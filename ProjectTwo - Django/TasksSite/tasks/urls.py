from django.urls import path
from tasks.views import home
from .views import TaskListView

urlpatterns = [
    path('', TaskListView.as_view(), name="tasks-home")
]