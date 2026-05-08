import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBuzxH2C9u7R47UWPqR_3_Rqxr-xd5a5cqXO5Qq4Sl-ObscHvtoe1teBd_093IKgPhaz2c7_QqdKLyBpmk5zUcXn8bUuuSHV6t2pF01Orw-clFdsL104Fuun4WM1ctvWT2aoHMJIaeIgRnMbsjIkQB2aynHJ9CoC5WOQws6NLdd9_kz6P1Sj9oDh3HPy3qktcaOg4tiIFpa0hwXRPVF8-AQCLjJwGFm9Pb9caRB6UTg6YjHNqHDU22HcfPJf4vMQ-Ik_0Xgk-DW4_0SZF4lG9n_QgOWjzKFp0AL8PJIQjxfX0dOrzHhYOJiLppHgEUXzSw6FgAciapbVnJtwZubTDP1rI='

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