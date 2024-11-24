import asyncio
from TelegramBot import TelegramBot


async def main():
    obj_telegram = TelegramBot()
    await obj_telegram.initialize()
    grupo_alvo = await obj_telegram.get_groups()
    membros = await obj_telegram.get_members_of_group(grupo_alvo)


if __name__ == "__main__":
    asyncio.run(main())
