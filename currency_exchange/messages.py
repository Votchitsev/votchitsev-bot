"""Модуль формирует сообщения для отправки их пользователю по обмену валюты."""

from .api import get_exchange_amount


def currency_question() -> str:
    """Возвращает вопрос по выбору валюты."""

    return "Выберите пожалуйста валюту для обмена"


def amount_question() -> str:
    """Возвращает вопрос по выбору количества валюты для обмена."""
    
    return "Введите количество валюты для обмена"


def currency_exchange(_from: str, to: str, amount: str) -> str:
    """
    Вызывает функцию get_exchange_amount,
    которая получает информацию об обмене валюты с api
    и возвращает сообщение с данной информацией.
    """

    exchange_sum = get_exchange_amount(_from, to, amount)

    if not exchange_sum:
        return False

    return f"На {amount} {_from} вы можете приобрести {exchange_sum} {to}."
