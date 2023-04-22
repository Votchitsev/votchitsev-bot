from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

import lang


router = Router()


@router.message(Command(commands=['start']))
async def show_menu(message: Message):
    await message.answer(text=lang.WELCOME_TEXT)
