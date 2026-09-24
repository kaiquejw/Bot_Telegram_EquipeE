import asyncio

from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 36016816  # Seu API ID
API_HASH = "9045f8b49a3f8d0a44163d584c2b133a"
SESSION = "1AZWarzcBux8FFeSpdCQmVgz-s3w6fOAgd1ixSVhv4abzKNL0LGDKVWEMAQejytpPwhTh7pem3LyamF8R6UW6btRquKbfXxCSEQqTs3B81Fu1wIIu-FhwY_nFRkLzaMqeVMePKBse1_8D3lI1zNVGmsoNQDhqQAMuy3bMNrbGNgMzJJo1u2xPJCdK5qlrTfEPnhsrCX-U5t_62BirP__0mtZ0gdyLiShqNWbAZ8o15B1d_c-Qv-v_RxdSha3RllWpWv11hMH9Tc5BxrCkrlsax_hJEPpqWRioaCdiLzRB8cV2b5HeQa6w_Objbi5Exv8qHllv0PvEEQMPI9pbPDtAvVhhjSIec00="


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
