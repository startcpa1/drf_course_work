from rest_framework import serializers

from habits.models import Habit
from habits.validators import RelatedOrRewardValidator, RelatedHabitValidator, NiceHabitValidator, \
    DurationHabitValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [RelatedOrRewardValidator(), RelatedHabitValidator(), NiceHabitValidator(),
                      DurationHabitValidator()]
