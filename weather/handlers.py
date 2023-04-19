from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

import messages

class City(StatesGroup):
    city = State()

router = Router()

@router.callback_query(Text('weather'))
async def weather(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(City.city)
    await callback.message.answer(
        messages.weather_city()
    )

@router.message(City.city)
async def process_city(message: Message, state: FSMContext) -> None:
   
    answer = messages.wether(message.text)

    if not answer:
        await message.answer('Что-то пошло не так...')
        await state.clear()

        return

    await message.answer(answer)
    await state.clear()
