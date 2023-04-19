import csv
from pprint import pprint
from api import get_weather


def weather_city():
    """Возвращает сообщение с вопросом о выборе города для определения погоды"""
    return 'В каком городе вы хотите узнать погоду?'

def wether(city):
    """Принимает аргумент - город и возвращает погоду"""

    coordinates = {}

    with open('data/city.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['city'].find(city) != -1:
                coordinates['latitude'] = row['geo_lat']
                coordinates['longitude'] = row['geo_lon']
        
    if not coordinates:
        return False

    weather = get_weather(coordinates)

    if not weather:
        return False
