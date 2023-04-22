"""Модулю взаимодействует по api c сервисом unsplash.com"""

import json

import requests

from config import ANIMAL_API_KEY


def get_animal() -> str:
    """Делает запрос на сервер unsplash.com и возвращает полученную ссылку на фотографию."""

    url = 'https://api.unsplash.com/photos/random?collections=28909082'

    header = {
        'Authorization': f"Client-ID {ANIMAL_API_KEY}",
    }

    params = {
        'collections': '28909082', # id коллекции со смешными животными
    }

    response = requests.get(url, headers=header, params=params)

    if not response.ok:
        return False
    
    photo_url = json.loads(response.text)['urls']['small']

    return photo_url
