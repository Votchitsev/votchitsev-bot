"""Модуль обрабатывает пользовательские действия по получению картинки животного"""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from .messages import animal


router = Router()


@router.message(Command('animal'))
async def animal_handler(message: Message) -> None:
    """
    Вызывает функцию messages.animal,
    которая возвращает ссылку на картинку.
    Если ссылка есть - отправляет в чат,
    если нет - возвращает сообщение об ошибке.
    """

    photo_url = animal()

    if not photo_url:
        await message.answer(
            'Что-то пошло не так...'
        )

    await message.answer_photo(photo_url)
