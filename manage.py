"""
Homework - 21

task_21_1: Написать сайт - предоставляет полный CRUD для работы с пользователями.
Модель пользователя состоит из id,firstname, lastname, age, profession.
На главной странице отображена краткая информация(id, firstname, lastname)
о всех пользователях. При нажатии на пользователя происходит перенаправление
на детализированную информацию по пользователю. На детализированной странице
пользователя есть кнопки позволяющие отредактировать и удалить пользователя.

Задание 7 (HW): После создания пользователя - перенаправлять на домашнюю страницу.
Добавить возможность переход на форму создания с домашней страницы.
"""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HW21.settings')
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
