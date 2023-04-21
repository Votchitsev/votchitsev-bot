from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery

from .messages import animal


router = Router()


@router.callback_query(Text('animal'))
async def animal_handler(callback: CallbackQuery) -> None:
    """
    Вызывает функцию messages.animal, которая возвращает ссылку на картинку.
    Если ссылка есть - отправляет в чат.
    """

    photo_url = animal()

    if not photo_url:
        await callback.answer(
            'Что-то пошло не так...'
        )

    await callback.message.answer_photo(photo_url)
