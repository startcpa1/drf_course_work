# Generated by Django 5.0.4 on 2024-04-09 19:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_alter_habit_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='start_time',
            field=models.TimeField(default=datetime.time(19, 14, 40, 758155), verbose_name='время'),
        ),
    ]
