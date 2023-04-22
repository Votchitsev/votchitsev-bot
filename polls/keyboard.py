"""Модуль инициализирует клавиатуру для создания опросов"""

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

builder = InlineKeyboardBuilder()


BTN_CONFIRM = InlineKeyboardButton(
    text='Да',
    callback_data=1,
)


BTN_CANCEL = InlineKeyboardButton(
    text='Нет',
    callback_data=0
)


builder.add(
    BTN_CONFIRM,
    BTN_CANCEL,
)
