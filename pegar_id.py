import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu2Rd29qSX4MCKOoAPsXkGU_R81XM2ThD4Xz-uGonr8uDnAypPUdpOb_24hY-F848S9hw8QfhaMBYXJO9pGnxCvPZ2DzqExtVUaTVWirCuxpxDflT6mz39MbFiIuFwcJdi_EEnQ4QIQV2ItQzZf_dfikmwsG_0hFETZ4aNgrZBolHqOh1CjuNBkKglq8ayLKA0psTXA-YPHVo_4DaUUsjaZ-0_nLOV18oAlosdsBpi2AiuT-VZqZ9Tsl4KaGxmuDUyd3hAawXUBw2vBW6ASUoByipml5Yv1qlnVeXqG9RqPTvIP0WQN4b0ZFBp-75iAYxQzdrywBH6irAnIgG8eYIu94='

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