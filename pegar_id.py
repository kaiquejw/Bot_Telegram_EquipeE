import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBux1jnikHJUs5z6g6kSojFrYbnV-YgRNItTIbAZBWG4MG_8WCzYj7iwjLcENMPDm19uLTVidd4-jb0rXWWDzraF0DVTY4JeREC2txicIPhdDblBRXdHu5OwHDEVdI0zM8tBhuX4OqqFwogT20x3VAEzv_0UNWMgcKhwU99GB2HbN7UzRruOp1iOW5tDJZQyIBS5FOtWgpvbYSkGyZRhHVj_IsentYuw2sT_fuJ6fCNyH3YkjtU2v3EWyzMltsk6prRSOLNj2UJIFmDCHg8TX7HI7q6HaupLrvVz90pOk2q0mPwvu8BnPFgfgaNOhnmB5JOZ2LDqamEXBiEVx1llxkGx4='

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

if __name__ == '__main__':
    asyncio.run(main())