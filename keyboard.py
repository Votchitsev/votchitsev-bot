from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

builder = InlineKeyboardBuilder()



BTN_WEATHER = InlineKeyboardButton(text='Погода', callback_data='weather')
BTN_CONVERT_CURRENCY = InlineKeyboardButton(text='Конвертировать валюту', callback_data='currency_exchange')
BTN_ANIMAL = InlineKeyboardButton(text='Милое животное', callback_data='animal')
BTN_POLLS = InlineKeyboardButton(text='Создать опрос', callback_data='polls')

builder.row(
    BTN_WEATHER,
    BTN_CONVERT_CURRENCY
)

builder.row(
    BTN_ANIMAL,
    BTN_POLLS,
)
