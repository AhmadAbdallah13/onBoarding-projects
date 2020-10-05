from django.shortcuts import render
from django.views.generic import ListView
from tasks.models import Tasks

# to get all the tasks a user has created: user.tasks_set.all() 
# "the user in the begining is a var that contanins the logged in user"


def home(request):
    queryset = Tasks.objects.all()
    context = {
        'shit' : queryset
    }
    return render(request, 'tasks/home.html', context)

class TaskListView(ListView):
    model = Tasks