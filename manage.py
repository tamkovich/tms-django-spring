"""
Homework - 19

task_19_1: Дана форма с тремя текстовыми полями.
Вернуть пользователю максимальное по длине значение поля.
Пример: введены abc, abcdef, ab - пользователю вернется abcdef.

task_19_2: Дана форма с одним полем - дата.
Если дата первое января - вывести сообщение: “С новым {номер года} годом”.
В ином случае, вывести дату в формате: год-месяц-день.

Homework - 20

task_20_1: Создать форму через django forms описывающую заказ авиабилета.
Форма должна содержать поля - имя, откуда, куда, сколько человек, дата.
При отправке данных пользователем проверять валидность данных,
если они валидны и количество человек 1 то вывести результат - "стоимость 100$",
если количество человек больше 1, то стоимость должна считаться по формуле
100*2*количество человек. Если данные не валидны, то вывести ошибку.
Задание выполняется в рамках одного приложения.
Должен быть создан отдельный файл urls.py в приложении, и отдельная папка templates.
"""

import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HW19.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
