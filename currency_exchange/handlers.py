import json
from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from .messages import currency_question, amount_question, currency_exchange
from .keyboard import builder


class CurrencyExchange(StatesGroup):
    currency = State()
    amount = State()


router = Router()


@router.callback_query(Text('currency_exchange'))
async def currency_exchange_handler(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(CurrencyExchange.currency)
    await callback.message.answer(
        text=currency_question(),
        reply_markup=builder.as_markup(),
    )

@router.callback_query(CurrencyExchange.currency)
async def process_currency(callback: CallbackQuery, state: FSMContext) -> None:
    await state.update_data(currency=json.loads(callback.data))
    await state.set_state(CurrencyExchange.amount)
    await callback.message.answer(
        text=amount_question()
    )

@router.message(CurrencyExchange.amount)
async def process_amount(message: Message, state: FSMContext) -> None:
    
    try:
        amount = int(message.text)
    except:
        await message.answer('Введите, пожалуйста, число')

    currency = await state.get_data()
    answer = currency_exchange(currency['currency']['from'], currency['currency']['to'], amount)

    if not answer:
        await message.answer('Что-то пошло не так...')
        await state.clear()
        return
    
    await message.answer(answer)
    await state.clear()
