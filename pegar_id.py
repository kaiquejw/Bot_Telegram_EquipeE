import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu8ErcTQ8RdJJqvUTAnZB_dzskPeNURplQ6BMnj0NeZYmIl-iAecufu9NhzJOKmS9yTzdDPEnGJlztRChFpfRFcTJd6owKRorZwbKbK0rCo7MeYMcyiSIc9NCU3dgJ9Pkhf1uM75YwT4ZsJfG1AcmgEB3LqekzTM3pBILPTETFK-wpph1TikXopM-7MtB7MCOCM8w42FD7f1z9XgvLx4TX0Y0cpxT7AcDVtCvZNdQOuOFGZbBKeAcx43-Woq5QeZmzt1YIDR3-HRNBXkQHQs7WbypD3JGA9jAHbV2toycVsGDF_lZJX2H6Ai7qY2UWjEA45pbBpkzzHxUZ1mKICRdprc='

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