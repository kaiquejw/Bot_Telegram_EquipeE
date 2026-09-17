import asyncio

from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 36016816  # Seu API ID
API_HASH = "9045f8b49a3f8d0a44163d584c2b133a"
SESSION = "1AZWarzMBuw_pEqfheOndFRd6mFHwnlxo1bTCovgTBVcTgLL8PkkUCRgTOFevbrHfTiBy9oUxc4k6Sk3tMXV5-9pAmmHr84l0zsEXgKEQDouz8arBrvuBm4-HagiRiHvzjed49wHdheb5twICirU2Ga0fDRgzRLle3rBxYVVTHPzIyPqMQ-TZFRWVSOCaJIHdkm5wRMEC9BmcpNRNWY1lsVv8YD45LlIx5Zyj5IuZFrdEb5lk8Ud52LBgDNEkPFbkXhIdW8Js-BciCRySmL06ygP8vA7rYzB82utjYcF98nD_cmZ-QHPQSoeXV8JlZ5zgKj9uVg9qZwN0pzVbyFVrjPUVaHEQllc="


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
