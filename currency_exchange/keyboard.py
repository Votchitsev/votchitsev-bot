"""Модуль инициализирует клавиатуру, которая используется в выборе валюты."""

import json

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


builder = InlineKeyboardBuilder()


BTN_RUB_EUR = InlineKeyboardButton(
    text='RUB -> EUR',
    callback_data = json.dumps({
        'from': 'RUB',
        'to': 'EUR',
    })
)


BTN_EUR_RUB = InlineKeyboardButton(
    text='EUR -> RUB',
    callback_data = json.dumps({
        'from': 'EUR',
        'to': 'RUB'
    })
)

BTN_RUB_USD = InlineKeyboardButton(
    text='RUB -> USD',
    callback_data = json.dumps({
        'from': 'RUB',
        'to': 'USD'
    })
)

BTN_USD_RUB = InlineKeyboardButton(
    text = 'USD -> RUB',
    callback_data = json.dumps({
        'from': 'USD',
        'to': 'RUB'
    })
)

builder.row(
    BTN_RUB_EUR,
    BTN_EUR_RUB,
).row(
    BTN_RUB_USD,
    BTN_USD_RUB,
)
