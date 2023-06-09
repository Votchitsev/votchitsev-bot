"""Модуль обрабатывает пользовательские действия по созданию опроса."""

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message

from .messages import question, option, confirm, chat_id
from .keyboard import builder
from main import bot
import lang


router = Router()


class Polls(StatesGroup):
    chat_id = State()
    question = State()
    options = State()
    confirm = State()


@router.message(Command('polls'))
async def polls_handler(message: Message, state: FSMContext) -> None:
    """
    Обрабатывает команду '/polls'. Отправляет сообщение для выбора id чата,
    в который нужно отправить опрос. Устанавливает состояние 'Polls.question'.
    """

    await state.set_state(Polls.chat_id)

    await message.answer(
        text=chat_id(),
    )


@router.message(Polls.chat_id)
async def chat_id_process(message: Message, state: FSMContext) -> None:
    """
    Обрабатывает сообщение с id чата. Отправляет сообщение для выбора вопроса.
    Устанавливает состояние 'Polls.question'.
    """

    await state.set_state(Polls.question)
    await state.update_data(chat_id=message.text)

    await message.answer(
        text=question(),
    )


@router.message(Polls.question)
async def question_process(message: Message, state: FSMContext) -> None:   
    """
    Обрабатывает сообщение пользователя с текстом вопроса (записывает в состояние).
    Отправляет сообщение пользователю с вопросом о выборе вариантов ответа.
    Устанавливает состояние 'Polls.options'.
    """

    await state.update_data(question=message.text)
    await state.set_state(Polls.options)

    await message.answer(
        text=option(),
    )


@router.message(Polls.options)
async def options_process(message: Message, state: FSMContext) -> None:
    """
    Обрабатывает сообщение пользователя с текстом вариантов ответа (записывает в состояние).
    Отправляет пользователю сообщение для подтверждения отправки опроса.
    """

    await state.update_data(options=message.text.split(';'))

    await state.set_state(Polls.confirm)

    data = await state.get_data()

    await message.answer(
        text=confirm(data['question'], data['options']),
        reply_markup=builder.as_markup(),
    )


@router.callback_query(Polls.confirm)
async def confirm_process(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Обрабатывает действие пользователя по подтверждению
    отправки формы.
    """

    confirm = bool(int(callback.data))

    data = await state.get_data()

    parsed_options = [option for option in data['options'] if len(option) > 0]

    if confirm:
        try:        
            await bot.send_poll(
                chat_id=data['chat_id'],
                question=data['question'],
                options=parsed_options,
                is_anonymous=False,
                allows_multiple_answers=False,
            )
        except:
            await callback.message.answer(
                text=lang.ERROR_MESSAGE,
            )

            return

        await state.clear()
        await callback.message.answer(
            text='Отправлено.',
        )

        return

    await state.clear()
    await callback.message.answer(
        text='Не буду отправлять.',
    )
