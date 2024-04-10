from rest_framework import generics

from habits.models import Habit
from habits.paginators import HabitsPaginator
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitCreateView(generics.CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()


class HabitDetail(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDeleteView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitListView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitsPaginator

    def get_queryset(self):
        """Список привычек пользователя"""
        return Habit.objects.filter(user=self.request.user)


class PublishedHabits(generics.ListAPIView):
    serializer_class = HabitSerializer

    def get_queryset(self):
        """Список публичных привычек"""
        return Habit.objects.filter(is_published=True)
