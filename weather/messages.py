"""Модуль формирует сообщения для ответа пользователю (погода)"""

import csv

from .api import get_weather
import lang


def weather_city() -> str:
    """Возвращает сообщение с вопросом о выборе города для определения погоды"""

    return 'В каком городе вы хотите узнать погоду?'


def weather(city: str) -> str:
    """Принимает аргумент - город и возвращает погоду"""

    coordinates = {}

    with open('data/city.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['city'].find(city) != -1:
                city = row['city']
                coordinates['latitude'] = row['geo_lat']
                coordinates['longitude'] = row['geo_lon']
        
    if not coordinates:
        return False

    weather = get_weather(coordinates)

    if not weather:
        return False

    return lang.WEATHER.format(
        city=city,
        temp=round(int(weather['temp'])),
        feels=round(int(weather['feels_like'])),
        pressure=round(int(weather['pressure']) * 0.75),
    )
