import asyncio

from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 36016816  # Seu API ID
API_HASH = "9045f8b49a3f8d0a44163d584c2b133a"
SESSION = "1AZWarzcBu5XxBoDk58uh5OtWjIbfGTEAUqnLb-756lB0ii9QGAMPia8578roo6fURcMlSKyq2DD0vyUJ1Z8EctZS-rQ3c9NP-chslR0aM5oXhe9lIgZYl6WIMzQQRYmKVuQPMSrvNufCz4Y_kXSaPxTNiihHVWSO_I6hfQZYXaNkI_scUVOexvSq5fdE1Mng-XpQ986i08Kmw5br_NRFBPhs9nsB9QDx5V7PExRhAbQVPjypYC9t8GXOP_-6FxQuWFWaTie_aSU4E1_xFe7A_BueAQMxdsU9WFQMRPEE04NQae516O3NUP8qp0RabI9fS1mq1xE4PGIjkhpb2ViAKMM1EsV1kBs="


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
