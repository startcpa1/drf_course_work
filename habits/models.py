from django.conf import settings
from django.db import models
from django.utils import timezone

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):

    CHOICE_FREQUENCY = [
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
        ('in 2 days', 'Раз в 2 дня'),
        ('in 3 days', 'Раз в 3 дня'),
        ('in 4 days', 'Раз в 4 дня'),
        ('in 5 days', 'Раз в 5 дней'),
        ('in 6 days', 'Раз в 6 дней'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user',
                             verbose_name='пользователь',
                             **NULLABLE)
    action = models.TextField(verbose_name='действие', **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='место', **NULLABLE)
    start_date = models.DateField(default=timezone.now().date(), verbose_name='дата начала')
    start_time = models.TimeField(default=timezone.now().time(), verbose_name='время')
    duration = models.DurationField(default='00:00:00', verbose_name='выполнять чч:мм:сс')
    frequency = models.CharField(choices=CHOICE_FREQUENCY, default='daily',
                                 verbose_name='периодичность')
    is_nice = models.BooleanField(default=False, verbose_name='признак приятной привычки', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='признак публикации')

    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='связанная привычка',
                                      related_name='good_habit', **NULLABLE)
    award = models.TextField(verbose_name='вознаграждение', **NULLABLE)

    def __str__(self):
        return f'Я буду {self.action} в {self.duration} в {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        # ordering = (id,)
