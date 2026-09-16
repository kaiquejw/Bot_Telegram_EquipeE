import asyncio
import os
import random
import time
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from telethon import TelegramClient, events, utils
from telethon.errors import (
    ChatWriteForbiddenError,
    FloodWaitError,
    SlowModeWaitError,
)
from telethon.sessions import StringSession
from telethon.tl.functions.messages import SendMessageRequest

# --- CONFIGURAÇÕES GERAIS ---
API_ID = int(os.environ.get("TELEGRAM_API_ID"))
API_HASH = os.environ.get("TELEGRAM_API_HASH")

TZ = ZoneInfo("America/Sao_Paulo")

# ⚠️ AJUSTE PARA O DIA DA SENHA ⚠️
HORA_ALVO = 16
MINUTO_ALVO = 50
SEGUNDO_ALVO = 0

# Quando o listener fica "armado" antes do horário (pra pegar abertura adiantada).
ANTECIPACAO_S = 2.0
# Desiste este tempo depois do alvo, se o aviso de abertura nunca vier.
DESISTIR_APOS_S = 180

# DIAGNÓSTICO: se True, imprime TODOS os updates que chegam do grupo na janela.
# Use True nos testes pra ver quais sinais o Telegram manda quando abre.
# Use False em produção (print no meio atrasa um tiquinho).
DEBUG_UPDATES = True

CONTAS = [
    {
        "nome": "Jake",
        "secret_name": "SESSION_JAKE",
        "chat_id": -5186073583,
        "msg": "Jakeline x Daniel raio 3",
    },
]


def _ids_do_canal(chat_id):
    """Retorna todas as formas possíveis do id (cru e marcado) pra casar em qualquer update."""
    cru, _ = utils.resolve_id(chat_id)  # id sem o -100
    return {cru, chat_id, -cru, abs(chat_id)}


def _refere_canal(update, ids):
    """True se o update fala do nosso grupo — cobre TODOS os formatos conhecidos."""
    # tenta vários atributos onde o id pode estar
    for attr in ("channel_id", "chat_id"):
        v = getattr(update, attr, None)
        if v is not None and v in ids:
            return True
    # dentro de .peer
    peer = getattr(update, "peer", None)
    if peer is not None:
        for attr in ("channel_id", "chat_id"):
            v = getattr(peer, attr, None)
            if v is not None and v in ids:
                return True
    # dentro de .message.peer_id
    msg = getattr(update, "message", None)
    pid = getattr(msg, "peer_id", None) if msg is not None else None
    if pid is not None:
        for attr in ("channel_id", "chat_id"):
            v = getattr(pid, attr, None)
            if v is not None and v in ids:
                return True
    return False


def _eh_fechado(e):
    s = str(e).lower()
    return (
        ("plain" in s)
        or ("forbidden" in s and "send" in s)
        or ("write" in s and "forbidden" in s)
    )


async def enviar_uma_vez(client, peer, msg, nome, random_id, vencido, t_evento):
    """Dispara UMA vez, o mais enxuto possível. Loga só DEPOIS do envio."""
    if vencido.is_set():
        return
    vencido.set()  # trava: só um envio por conta
    t0 = time.monotonic()
    try:
        await client(SendMessageRequest(peer=peer, message=msg, random_id=random_id))
        # --- daqui pra baixo é só log, o envio já saiu ---
        t_done = time.monotonic()
        rtt = (t_done - t0) * 1000
        reacao = (t0 - t_evento) * 1000 if t_evento else -1
        agora = datetime.now(TZ).strftime("%H:%M:%S.%f")
        print(f"🏆 {nome} ENVIOU! ({agora}) rtt~{rtt:.0f}ms | reação~{reacao:.1f}ms")
    except ChatWriteForbiddenError:
        vencido.clear()  # ainda fechado -> libera pra tentar de novo no próximo sinal
        if DEBUG_UPDATES:
            print(f"   {nome}: sinal veio mas grupo ainda fechado")
    except FloodWaitError as e:
        print(f"🛑 {nome} FLOOD {e.seconds}s")
    except SlowModeWaitError as e:
        print(f"🐌 {nome} slowmode {e.seconds}s (já enviada)")
    except Exception as e:
        if _eh_fechado(e):
            vencido.clear()
            if DEBUG_UPDATES:
                print(f"   {nome}: sinal veio mas ainda fechado ({type(e).__name__})")
        else:
            vencido.clear()
            print(f"⚠️ {nome} erro: {e}")


# --- FASE 1: conecta e valida ---
async def conectar(conta):
    session = os.environ.get(conta["secret_name"])
    if not session:
        print(f"❌ {conta['nome']}: SESSION não encontrada no .env")
        return None
    client = TelegramClient(StringSession(session), API_ID, API_HASH)
    try:
        await client.connect()
        await client.get_dialogs()
        if not await client.is_user_authorized():
            print(f"❌ {conta['nome']}: login falhou (não autorizado)")
            await client.disconnect()
            return None
        peer = await client.get_input_entity(conta["chat_id"])
        ids = _ids_do_canal(conta["chat_id"])
        random_id = random.randrange(-(2**63), 2**63 - 1)
        print(f"✅ {conta['nome']} pronto | DC {client.session.dc_id} | ids {ids}")
        return (client, peer, ids, random_id, conta)
    except Exception as e:
        print(f"❌ {conta['nome']}: erro ao conectar — {e}")
        if client.is_connected():
            await client.disconnect()
        return None


# --- FASE 2: só listener ---
async def sniper(dados, alvo):
    client, peer, ids, random_id, conta = dados
    nome = conta["nome"]
    msg = conta["msg"]
    on_update = None
    try:
        vencido = asyncio.Event()
        janela = {"on": False}
        pendentes = []

        async def on_update(update):
            if not janela["on"] or vencido.is_set():
                return
            try:
                if _refere_canal(update, ids):
                    t_evento = time.monotonic()
                    if DEBUG_UPDATES:
                        ag = datetime.now(TZ).strftime("%H:%M:%S.%f")
                        print(f"📨 {nome} {ag} update: {type(update).__name__}")
                    pendentes.append(
                        asyncio.create_task(
                            enviar_uma_vez(
                                client, peer, msg, nome, random_id, vencido, t_evento
                            )
                        )
                    )
            except Exception:
                pass

        client.add_event_handler(on_update, events.Raw)

        # espera econômica
        while (alvo - datetime.now(TZ)).total_seconds() > 15:
            await asyncio.sleep(1)
        try:
            await client.get_me()  # esquenta o socket
        except Exception:
            pass

        inicio = alvo - timedelta(seconds=ANTECIPACAO_S)
        deadline = alvo + timedelta(seconds=DESISTIR_APOS_S)
        while datetime.now(TZ) < inicio:
            r = (inicio - datetime.now(TZ)).total_seconds()
            await asyncio.sleep(0.05 if r > 0.5 else 0.005)

        janela["on"] = True
        print(f"👂 {nome} OUVINDO (listener puro)...")

        # Backup: se já estiver aberto ao armar, tenta uma vez na hora
        try:
            await client(
                SendMessageRequest(peer=peer, message=msg, random_id=random_id)
            )
            vencido.set()
            print(f"🏆 {nome} ENVIOU (já estava aberto ao armar)")
        except Exception:
            pass  # fechado, ok — o listener cuida

        # só espera o listener disparar (ou o tempo esgotar)
        while not vencido.is_set() and datetime.now(TZ) < deadline:
            await asyncio.sleep(0.02)

        await asyncio.gather(*pendentes, return_exceptions=True)
        if not vencido.is_set():
            print(f"❌ {nome}: nada enviado — o sinal de abertura não veio/não casou.")

    except Exception as e:
        print(f"❌ Erro fatal {nome}: {e}")
    finally:
        if on_update is not None:
            try:
                client.remove_event_handler(on_update, events.Raw)
            except Exception:
                pass
        if client.is_connected():
            await client.disconnect()


async def main():
    agora = datetime.now(TZ)
    alvo = agora.replace(
        hour=HORA_ALVO, minute=MINUTO_ALVO, second=SEGUNDO_ALVO, microsecond=0
    )
    if alvo < agora:
        alvo += timedelta(days=1)

    print(
        f"🎯 [LISTENER PURO] Alvo: {alvo.strftime('%d/%m %H:%M:%S')} BRT | "
        f"agora {agora.strftime('%H:%M:%S')} | faltam {(alvo - agora).total_seconds():.0f}s"
    )
    print(
        f"⚙️  antecipacao={ANTECIPACAO_S}s | debug={DEBUG_UPDATES} | contas={len(CONTAS)}"
    )
    print("\n🔌 FASE 1 — Conectando contas...\n")

    resultados = await asyncio.gather(*(conectar(c) for c in CONTAS))
    prontas = [r for r in resultados if r is not None]
    falhas = [CONTAS[i]["nome"] for i, r in enumerate(resultados) if r is None]

    print(f"\n{'=' * 45}")
    print(
        f"✅ Prontas ({len(prontas)}): {', '.join(d[4]['nome'] for d in prontas) or '—'}"
    )
    print(f"❌ Falharam ({len(falhas)}): {', '.join(falhas) or '—'}")
    print(f"{'=' * 45}\n")

    if not prontas:
        print("❌ Nenhuma conta conectou. Encerrando.")
        return
    if falhas:
        print("🛑 ENCERRANDO — corrija as contas acima e reinicie o bot.")
        return

    print(f"🚀 FASE 2 — Listener ativo com {len(prontas)} conta(s)...\n")
    await asyncio.gather(*(sniper(d, alvo) for d in prontas))


if __name__ == "__main__":
    asyncio.run(main())
