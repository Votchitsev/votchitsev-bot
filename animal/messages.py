"""Модуль формирует сообщения для пользователя по получению картинки животного"""

from .api import get_animal


def animal() -> str:
    """Получает с api ссылку на фотографию и возвращает её"""

    animal = get_animal()

    if not animal:
        return False

    return animal
