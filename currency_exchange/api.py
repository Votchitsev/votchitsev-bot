import json

import requests

from config import CURRENCY_API_KEY


def get_exchange_amount(from_, to, amount):
    url = 'https://api.apilayer.com/exchangerates_data/convert'

    params = {
        'from': from_,
        'to': to,
        'amount': amount
    }

    header = {
        'apikey': CURRENCY_API_KEY,
    }

    response = requests.get(url, params=params, headers=header)

    if not response.ok:
        return False
    
    return json.loads(response.text)['result']
