"""Модуль взаимодействует по api с openweathermap.org"""

from config import WEATHER_API_KEY
import requests
import json


def get_weather(coordinates: dict) -> dict:
    """
    Получает с сервера информацию о погоде.
    """

    url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'lat': coordinates['latitude'],
        'lon': coordinates['longitude'],
        'appid': WEATHER_API_KEY,
        'units': 'metric',
    }

    response = requests.get(url, params=params)

    if not response.ok:
        return False
    
    return json.loads(response.text)['main']
