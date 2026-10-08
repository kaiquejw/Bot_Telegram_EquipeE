import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest

# --- PREENCHA COM SEUS DADOS ---
API_ID = 31891041  
API_HASH = 'df20f87a534f0a73f437cb33985d1c95' 

# Cole aqui a string gigante da conta que você quer colocar no grupo
STRING_DA_SESSAO = '1AZWarzcBuwt4gVT-Wxd2lWea2cSF6kTmolpwfxwoL7A9AptnPzhB6UUVwo4vXCTmeOcEWTBfsxpJM5ABp0w95tUJW4fvPjeaHEVATecdx-yV_yYrA9U8lbMc5P0n5Xuphvxw5p5gZT0Yj9Y0qzs6GJVaIdgUb4zco77LNMyygPMSTleJyokM_Y_edIOBopZgERi_WZh6D6TilhHDJwmQto8ybTnVvoZqbZBQivqv3dBe9JcNMfGtg1An9suHXAPuwA_KO1-dmDseRlzYkbxQw2jXIt9BSlHrkBECT-Pd50btqQGxExLoiFwe2cKXGWk0YSe2su6OlTpk4mXW1Q94xJ8Jd_2v7TQ=' 

# Link do grupo (ex: 'https://t.me/+XyZ123...' ou '@meugrupo')
LINK_DO_GRUPO = 'https://t.me/+kBc0ls8gJ9c5NjBh'

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