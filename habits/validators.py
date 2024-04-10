from datetime import timedelta

from rest_framework.exceptions import ValidationError

from habits.models import Habit


class RelatedOrRewardValidator:
    """"Исключить одновременный выбор связанной привычки и указания вознаграждения"""

    def __call__(self, value):
        if value.get('related_habit') and value.get('award'):
            raise ValidationError('Одновременный ввод полей невозможен, выберите одно поле')


class RelatedHabitValidator:
    """В связанные привычки могут попадать только привычки с признаком приятной привычки."""

    def __call__(self, value):
        related_habit = value.get('related_habit')
        if related_habit:
            temp = Habit.objects.filter(id=related_habit.id).is_nice
            if not temp:
                raise ValidationError(
                    'В связанные привычки могут попадать только привычки с признаком приятной привычки')


class NiceHabitValidator:
    """Проверить что у приятной привычки не может быть вознаграждения или связанной привычки."""

    def __call__(self, value):
        if value.get('is_nice'):
            if value.get('related_habit') or value.get('award'):
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')


class DurationHabitValidator:
    """Время выполнения должно быть не больше 120 секунд."""
    def __call__(self, value):
        if value.get('duration') > timedelta(minutes=2):
            raise ValidationError('Время выполнения должно быть не больше 120 секунд')
