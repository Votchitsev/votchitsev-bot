from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

import config
from keyboard import builder


router = Router()


@router.message(Command(commands=['start']))
async def show_menu(message: Message):
    await message.answer(text=config.WELCOME_TEXT, reply_markup=builder.as_markup())
