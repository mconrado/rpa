import asyncio
from TelegramBot import TelegramBot


async def main():
    obj_telegram = TelegramBot()
    await obj_telegram.initialize()  # Chama o método de inicialização


if __name__ == "__main__":
    asyncio.run(main())
