import asyncio

from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 36016816  # Seu API ID
API_HASH = "9045f8b49a3f8d0a44163d584c2b133a"
SESSION = "1AZWarzMBuyyYx-2JxmKy5kc4mwNcfka8TUfIBHzwmJsAWIPM2zYJdZiQdbEcRRA0a0zI445fxBaobLRqy8H0MRqXDPFczmZSSLSMp6kP87OCwtAYGQJZt-2o0_4X7DobiKmiNhWULDP5wlFU5wNxFws72ZxAiZUSQScD-KUGxIeEfRRc9hRqaEazxefLbVD5bQbiBehCjqoE1MOpVpfnZauhq0Sw3pAosoP4WG4OYjwB6Tz_Im2aD7kUpSTyjF4hZh4wcql0OcmJSbk4vAZm4av_cUeCW0OBWR5O9cKv9-ZN2fqdpRno95-v1WFKTESOCUI2ibwRyaho1C51J2xgF_H4ScrVqzI="


async def main():
    print("Conectando...")
    client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
    await client.connect()

    print("\n👇 AQUI ESTÃO SEUS ÚLTIMOS GRUPOS/CONVERSAS 👇\n")
    print(f"{'NOME DO GRUPO':<30} | {'ID PARA O GITHUB'}")
    print("-" * 50)

    # Pega as últimas 15 conversas
    async for dialog in client.iter_dialogs(limit=15):
        print(f"{dialog.name:<30} | {dialog.id}")

    print("\n👆 Copie o ID (número negativo) do grupo 'Teste' e coloque no GitHub.\n")


if __name__ == "__main__":
    asyncio.run(main())
