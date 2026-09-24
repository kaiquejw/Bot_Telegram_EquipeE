import asyncio

from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 36016816  # Seu API ID
API_HASH = "9045f8b49a3f8d0a44163d584c2b133a"
SESSION = "1AZWarzMBu3igDtkLfrkgMMKeN6ZdCdKGLK1B6T4Na_vE5_CTeeSxB70IB0VpQrjiCnfD9MAi6gW7wgiDOFUqL0nv7BHP8sTGKruVJjlj5g6k4knXTymwklv-_4ymF5dfNsshH3OoS--ltpM3YLjArZXb7_CS7pZyNHmxX8oLneMYlK7Rp5-VWIukF2rry9lgJpBtZ10ELeI0RjYFxJBZh0dEkUlt-0PSrlehfcpy5ilSA-8JfCkeX1I-w7oddbjy6wQheMbprKWBKwQ9y0pZD1KCXZnsWQ0KvqyYeTZOI9tv-fAOhEedlsETY7dhX1jK3zOZogKTMhyI3zqZrygAWVpJCPXPTQI="


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
