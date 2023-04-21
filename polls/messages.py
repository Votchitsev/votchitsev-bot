def question():
    return 'Введите вопрос для опроса.'


def option():
    return 'Введите варианты ответа через запятую.'


def confirm(question, options):
    
    message = 'Отправить опрос в таком виде?\n\n'

    message += f"{question}\n\n"
    
    for option in options:
        message += f"{option}\n"

    return message
