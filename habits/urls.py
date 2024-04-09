from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateView, HabitDeleteView, HabitUpdateView, HabitDetail, HabitListView, PublishedHabits

app_name = HabitsConfig.name


urlpatterns = [
    path('habit/create/', HabitCreateView.as_view(), name='habit-create'),
    path('habit/delete/<int:pk>/', HabitDeleteView.as_view(), name='habit-delete'),
    path('habit/update/<int:pk>/', HabitUpdateView.as_view(), name='habit-update'),
    path('habit/<int:pk>/', HabitDetail.as_view(), name='habit-detail'),
    path('habit/list/', HabitListView.as_view(), name='habit-list'),
    path('habit/published/', PublishedHabits.as_view(), name='habit-published')
]
