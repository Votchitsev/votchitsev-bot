from config import WEATHER_API_KEY
import requests
import json


def get_weather(coordinates):

    # url =  f"https://api.openweathermap.org/data/2.5/weather?"
    # f"lat={coordinates['latitude']}&lon={coordinates['longitude']}&"
    # f"appid={WEATHER_API_KEY}"

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
