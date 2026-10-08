import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest

# --- PREENCHA COM SEUS DADOS ---
API_ID = 31891041  
API_HASH = 'df20f87a534f0a73f437cb33985d1c95' 

# Cole aqui a string gigante da conta que você quer colocar no grupo
STRING_DA_SESSAO = '1AZWarzcBu4Vz1pk7wG4BrNlw9eJ7GzT6e13cbrFAl3_3Tb9-9jS8r7uxrkEcD_FL5WUdn6tmXQkKtBxFAeAFYpFB4OZ5sho6lu9q9UVY0pdxB_9DxV8Fs38_Abs5L424wiFBO2bADd2a7NdL9VE2YfZtG9EpxRS4cmjkB5HzDbY44pmfyVti2xyTA3Auy205QSxcYSSYCP-noumrZrnOxHO6-jOsHG7eJ4yJ6wxB_-AWXfDeeJZez_lIi5pNhlcXuSW2zHGy6hBOzs1_1SuZQkRT8xSyUZ1RTkOqLJw5Srj4pq3I6zH80MsiBtRLQ9i7VaRi3XYUsxCL5cJzFnvPO0e5zTveO6w=' 

# Link do grupo (ex: 'https://t.me/+XyZ123...' ou '@meugrupo')
LINK_DO_GRUPO = 'https://t.me/+yxr8qg_LaFU4Yzkx'

async def entrar_no_grupo():
    client = TelegramClient(StringSession(STRING_DA_SESSAO), API_ID, API_HASH)
    
    await client.connect()
    if not await client.is_user_authorized():
        print("❌ Sessão inválida ou desconectada. Gere uma nova.")
        return
        
    print(f"✅ Conta conectada! Tentando entrar em: {LINK_DO_GRUPO}")

    try:
        if "+" in LINK_DO_GRUPO or "joinchat" in LINK_DO_GRUPO:
            # Lógica para links privados
            hash_convite = LINK_DO_GRUPO.split('+')[-1] if '+' in LINK_DO_GRUPO else LINK_DO_GRUPO.split('/')[-1]
            await client(ImportChatInviteRequest(hash_convite))
        else:
            # Lógica para links públicos
            await client(JoinChannelRequest(LINK_DO_GRUPO))
            
        print("🎉 SUCESSO! A conta entrou no grupo.")
        
    except Exception as e:
        print(f"⚠️ Erro ao tentar entrar: {e}")
        
    finally:
        await client.disconnect()

if __name__ == '__main__':
    asyncio.run(entrar_no_grupo())