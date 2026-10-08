import asyncio

from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 36016816  # Seu API ID
API_HASH = "9045f8b49a3f8d0a44163d584c2b133a"
SESSION = "1AZWarzMBuwftQrgHz_GUmRZzAnuHOcqSo1jVNXL2i-tXJlKSOnlFSsv0_HnF__Bgb-HmtyRXyX5wt4CPRI_iQsMmRgOGYM-jsvJEoeI8j5Z0o_Cyv1kkhUYy9-tLcnXYrkArQu8cFmj2uyfEN97R9whjmV-QIgJerVkUXe1-qEC8z_ax9MEoakUvBP-HYepQWS1qzrJMBRkJcIuRIQ72bcBa_gTK80x66E_R5hBXvgRQXqP0JmGPgJnZq3BittTHphIjWfl5ewpvX7Zkn_92E0MdAB0U-lvZL-8NX7d28fYPOqG6HJajLE832CpYeN5Ukoh72TnWF4bWGM_gB_OpkbztgkyD1Y0="


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
