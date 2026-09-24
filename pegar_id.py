import asyncio

from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 36016816  # Seu API ID
API_HASH = "9045f8b49a3f8d0a44163d584c2b133a"
SESSION = "1AZWarzcBuyTggPWm60yBJRkshqNyHoBTUsBndbh1Uzewkbt6n6n0i4bFZzjFUn_obfwEuqdOSIHsSOqCsG9Gmo98_MgJQI6L_ml2Cda-Q5FYApdya9VtCuXwGzngBHmKmvPH6vfKDlphVRuU0bTBcfcPvsXPQx1mrGiLfuNWWpCWbhy0fHUQizrvMnC7EUlnhYfjqrFfIYOu-OJn1uLZNRr6OMdMUVOpA_gvgoyJDm-ecBg_VgeqFx3bCOLYcsrDzEI1NtJgjPRNJjTcLQRooGLEN9De4bApQdHhHDNvQuQ40ZRn7MfBp6QBC8j3X5tAQMKkLjsobILCH__2IIzMz3cK4aO2Or0="


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
