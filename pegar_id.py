import asyncio

from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 36016816  # Seu API ID
API_HASH = "9045f8b49a3f8d0a44163d584c2b133a"
SESSION = "1AZWarzcBuxUBbalZ21P3eoG0gwZ3WVEXCNc9DmZ4iXdQWoviQuF4YLIWy_yYHkvZnyODwnyK7hoZaz6h3g7vx5Kp79TG6G2H4CESkQYJU1StfexWxf_yTlnSXoRHEay8SyNw9eVGXP9CjsmK5dLHY9UmsSMp_dgE9ULaHNLRFDI1VB78VzItgWiKy7QudUiQbNJ0Z6FFhMkKxTuudVYOBlJjpGuBCEHnLHC8gsVfwMqteOjSFnlRA2G7PVDNCzbYmbBEeWJ6S2I31c4TU_BIQi1AQKKO7-1OSGkAJ0cDahKVMNyKhvdlrR7wPi2rSVgTnn_cPVK1h8bu_c1ClyNRXSI19kmyyQo="


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
