from config import WEATHER_API_KEY
import requests


def get_weather(coordinates):

    url =  f"https://api.openweathermap.org/data/2.5/weather?"
    f"lat={coordinates['latitude']}&lon={coordinates['longitude']}&"
    f"appid={WEATHER_API_KEY}"

    response = requests.get(url)

    data = response.json()

    if data['cod'] == '401':
        return False