import asyncio

from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 36016816  # Seu API ID
API_HASH = "9045f8b49a3f8d0a44163d584c2b133a"
SESSION = "1AZWarzMBuzVWjJjmpVu_pmMItsUV6A_yWjO5EqH1dY-LaNuozvJo6-qAXscniQ-MF1ImUZDnIN9qSswXU8jZowjV0dcYRFNFtVn9fKR-GStHS-60641gI_boCdmsaw96hiVtePWlWIwBMdhIWa08b-8a2nfvQZq0xHO2GB-fiiStIGXRVr5GsJzs5WKnR6wxHBJ197Km3pG1cqrltyI40HmSKPtSBZs15mcivRfHCbEoWWk3yMv9Cr2aR2ZK8Owkab4RRqYF6QkMalr9_akryk5wAnYmcJCcSHkhqZWP5Mr4CTl1Cc-qCMXORLe-OozpaBGGzk8SkKWHv-mZB7AbC6HH_gqSkF8="


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
