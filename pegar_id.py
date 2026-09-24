import asyncio

from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 36016816  # Seu API ID
API_HASH = "9045f8b49a3f8d0a44163d584c2b133a"
SESSION = "1AZWarzMBu5idqFEeMs4lmubtj2ohfVL6znmYxmgCIzgNtqyngFEIWZM9eR1SamZYAhobmoIBULJ29uA6vyU2PTG1ab2efCxUSR4qH7R2s6YRKiRcASZoOP4NBTgTyeqaPbBgaHE0O_SN6ER3sR7-Ojl9iPhdDOEekkegQIc-rJiuMyVNr0fS8foIkyymG8eNVMnwuZvcnmhMNSrEu-DYANwzQ8uLp95OTzc_aF2cUbG7-oNuTqjzb3NUigzqzn1dWmTACJC1C_CqAywOWbgArdTZQRPMi4ynattaeaVqfK3GQbm-HaMsA7aP8ssie5pZiiQ0HGnsbIfa4Z-_DEwfCxFp0ifScOs="


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
