import asyncio

from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 36016816  # Seu API ID
API_HASH = "9045f8b49a3f8d0a44163d584c2b133a"
SESSION = "1AZWarzgBu1UMWAjlb2pZPi-TrojAWYcDO8a0X_kL26jWK7prVO4AXdZ7vA-lz1zb9h-3um_nImDocG-ja32YZPQh4pp6lYRfOTRTZqXzzuoGuu9MmvZ89tGPk1_xetycKM6kG3SPAKlz8Rcir2or6yLsLMho1wP3cZsHFXsa8_HDbkQcQtwlDt1kxsNOErF_xoa6HekJWVhvx7N7q_-HWkrLlkMtl51LbI0QKtMsxG-66GvZ_W4Ql1lImgAbL_eXMH3J5QqmaBH0bFAJw8pZ1RkkLeFXUiIZV6UDLTDHX0odPIRJlXnbu-gEcsO3-7LjZqPO-EWohAOFjGdZGXhnID6Nwyb4Kq0="


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
