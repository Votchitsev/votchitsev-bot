from aiogram import Bot, Dispatcher

from aiogram.fsm.storage.memory import MemoryStorage


import asyncio
import config
import handlers
from weather import handlers as weather_handlers


async def main():
    bot = Bot(token=config.BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.include_router(handlers.router)
    dp.include_router(weather_handlers.router)

    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    asyncio.run(main())
    