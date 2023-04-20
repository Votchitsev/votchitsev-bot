from .api import get_exchange_amount


def currency_question():
    return "Выберите пожалуйста валюту для обмена"


def amount_question():
    return "Введите количество валюты для обмена"


def currency_exchange(_from, to, amount):
    exchange_sum = get_exchange_amount(_from, to, amount)

    if not exchange_sum:
        return False

    return f"На {amount} {_from} вы можете приобрести {exchange_sum} {to}."
