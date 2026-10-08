import asyncio

from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 36016816  # Seu API ID
API_HASH = "9045f8b49a3f8d0a44163d584c2b133a"
SESSION = "1AZWarzMBu6i60iA323cV9VFcaiQN0DhMYGfgykF5vQBEsyTHSGHEXuRiHOfOIX2M7Zn04AzYkDmWVOPOj1PiTfU8fWz4ZsSWTerxXe-0XM3mQDDj136Q24ugkni3em4SUbP9n3wDZS_dlVtBrLv8fqdQBkAUuexkzIa2GJJ0umZxrpCzVC_2iGgn3DzCYLi_jWiJeF6bi7i6KXvY4IA9BA2vee8YyE7swNlfFw_yNxbpt7jXJS1zdFpOarqZsU4x7rJvhvZOk1meKiguV5v9w7TUGpQcuALg0te1gD0SEcwc8zebRHecu3aoPnTZ_sZA7xXDGEgeGCrOrvWQftyK_WDyuh-KP4Q="


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
