import asyncio

from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 36016816  # Seu API ID
API_HASH = "9045f8b49a3f8d0a44163d584c2b133a"
SESSION = "1AZWarzMBu6WXJ9F0g8vQAy5j47g8j5x69aB-ya3tiwEHsumWBZIuF0Zn1B2FZnwmmd4rG5c2NOcjI2RCZVgJ8umP9vUZIvREn6X3CcGMwtJYoayKszmEd9ElMYSqH9OCmjPsLbFlO2iZrbuc7qkrDXxOi8H6Bxrhl7U2R4C3wwWBIFWkgWUNL58D-OHWiM4NLiRslVkidtdghcgvU6cXj7U2OVtNHCDdZRtlz2aqtei4ggwi1dy9BykW29Vx_vZtrSYUPBEQ_9qTvySmmJXXWrOOEzyxE2AIVxhDkBUF3vKba86wDUUEcV4M5FeidgMgLSo57fbBhqjGOVCnik1HG48Itvts9J8="


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
