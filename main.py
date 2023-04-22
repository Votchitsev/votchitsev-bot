"""Основной модуль."""

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from aiogram.types import BotCommand

import config
import handlers
from weather import handlers as weather_handlers
from currency_exchange import handlers as currency_exchange_handlers
from animal import handlers as animal_handlers
from polls import handlers as polls_handlers


bot = Bot(token=config.BOT_TOKEN)


async def main():
    """
    Инициализирует MemoryStorage, Dispatcher,
    подключает обработчики, устанавливает команды
    для меню и запускает бота.
    """

    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.include_router(handlers.router)
    dp.include_router(weather_handlers.router)
    dp.include_router(currency_exchange_handlers.router)
    dp.include_router(animal_handlers.router)
    dp.include_router(polls_handlers.router)

    await bot.set_my_commands([
        BotCommand(command='start', description='Начать ➡️'),
        BotCommand(command='weather', description='Узнать погоду в городе 🌤️'),
        BotCommand(command='currency', description='Узнать курс валют 💰'),
        BotCommand(command='animal', description='Картинка смешного животного 🐾'),
        BotCommand(command='polls', description='Создать опрос и отправить в группу 📊')
        ])

    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    asyncio.run(main())
    