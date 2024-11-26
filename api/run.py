import asyncio
from TelegramBot import TelegramBot


async def main():
    obj_telegram = TelegramBot()
    print("Iniciando o robô...")
    print("Escolha o grupo alvo")
    await obj_telegram.initialize()
    grupo_alvo = await obj_telegram.get_groups()
    membros = await obj_telegram.get_members_of_group(grupo_alvo)
    print("%s membros encontrados no grupo" % len(membros))

    print("Escolha o grupo que você quer adicionar os novos membros")
    meu_grupo = await obj_telegram.get_groups()

    for membro in membros:
        adicionado = await obj_telegram.add_member_to_group(membro, meu_grupo)
        if adicionado:
            print("Membro %s adicionado com sucesso" % membro.id)


if __name__ == "__main__":
    asyncio.run(main())
