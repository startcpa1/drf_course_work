from datetime import timedelta

from django.conf import settings
import requests


class MyBot:
    """Класс для работы с уведомлениями в телеграм"""

    URL = f'https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}'

    def send_message(self, chat_id, text):
        path = f'{self.URL}/sendMessage'
        requests.post(url=path, data={'chat_id': chat_id, 'text': text})


def change_start_date(habit):
    """Функция меняет дату следующего выполнения привычки в зависимости от
    установленного периода"""
    if habit.frequency == 'daily':
        habit.start_date += timedelta(days=1)
    elif habit.frequency == 'in 2 days':
        habit.start_date += timedelta(days=2)
    elif habit.frequency == 'in 3 days':
        habit.start_date += timedelta(days=3)
    elif habit.frequency == 'in 4 days':
        habit.start_date += timedelta(days=4)
    elif habit.frequency == 'in 5 days':
        habit.start_date += timedelta(days=5)
    elif habit.frequency == 'in 6 days':
        habit.start_date += timedelta(days=6)
    elif habit.frequency == 'weekly':
        habit.start_date += timedelta(days=7)
    habit.save()