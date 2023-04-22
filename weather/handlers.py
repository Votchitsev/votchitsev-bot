"""Модуль обрабатывает пользовательские действия по получению погоды."""

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from . import messages


class City(StatesGroup):
    city = State()


router = Router()


@router.message(Command('weather'))
async def weather_handler(message: Message, state: FSMContext) -> None:
    """
    Устанавливает состояние City.city
    и отправляет пользователю вопрос о выборе города
    """

    await state.set_state(City.city)
    await message.answer(
        messages.weather_city()
    )


@router.message(City.city)
async def process_city(message: Message, state: FSMContext) -> None:
    """
    Обрабатывает ответ пользователя с выбором города:
    вызывает функцию messages.weather для получения текущей 
    погоды с сервера. Если ответ корректный - отправляет пользователю,
    если нет - сообщение об ошибке.
    """

    answer = messages.weather(message.text.capitalize())

    if not answer:
        await message.answer('Что-то пошло не так...')
        await state.clear()

        return

    await message.answer(answer)
    await state.clear()
