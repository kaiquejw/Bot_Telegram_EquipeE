import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu222QVc94HDMYxcOSG4x5ZwK0irK7-MOIy1aKihOqA7a0B48fd0Y7XyfZEfpw2x3ghbHs2waxzT4tFs2xQ1OHY0vwiNbhIfytKsJ9_ueZRU3dHoBv0dlm36HpfGcpHgiMOnmwsgD7H53z5R1O-FmJY_Xxdj1FOc-jR-dob1i0lCuRcNzB-AUXspWaWMTNwQMHw-fiT2rhXuXC44oHaL7q-RRCz0bkDFJh0sYVr0MgJG7urxVCBE5Nb6Wa_QacU1pVamVfNb-c3NML2jKKe3SL-0OcOBVIcr9Jx5S8BjA9WTJz434CRDb307NxA6qqDzMNnS-tCng4rqZPm42lcXv6b8='

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