from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from tasks.models import Tasks

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class TaskListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Tasks
    template_name = 'tasks/home.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Tasks.objects.filter(creator=self.request.user).order_by('-created_at')

class TaskCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Tasks
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return "/"

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = '/login/'
    model = Tasks
    fields = ['title', 'description', 'done']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return "/"

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.creator:
            return True
        return False

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = '/login/'
    model = Tasks
    success_url = '/'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.creator:
            return True
        return False