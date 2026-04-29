import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBuyKxOOmZncpGnv3eQR2UQrQ1y2efxRMLkhAUm-l5t3kD0IDIC69oDWhGa9PnQK892cp5T2OUuW27p7Qf2VALhim4DZ9A4JmZ0Zrbddd7LQzgSwsoRPT0WiFL2Aus95ZX0PMi0l2kd3CZDxzAhRR5yuxAG1UUwE-bzoUEKqorHH8eozhj3l3cyuXgrxNPLR-q4DABXGHQHpfSudpP0JhG6uu7R1luYqcDwjMZCJooaUaBfynmG5xHAXritSgMpXKKJvV_ZA9g-99avAQVk-tkHFsxiEx45dtt4zbowDbBhu1f8vLP3roUTfbWFnA7rL-ucJpMTlKYReehbM6U1XSnYTY='

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