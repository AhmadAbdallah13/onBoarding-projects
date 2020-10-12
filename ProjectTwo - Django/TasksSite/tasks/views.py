from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from tasks.models import Tasks

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class TaskListView(ListView):
    model = Tasks
    template_name = 'tasks/home.html'
    context_object_name = 'tasks'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Tasks.objects.filter(creator=self.request.user).order_by('-created_at')

class TaskCreateView(CreateView):
    model = Tasks
    fields = ['title', 'description']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return "/"

class TaskUpdateView(UserPassesTestMixin, UpdateView):
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
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class TaskDeleteView(UserPassesTestMixin, DeleteView):
    model = Tasks
    success_url = '/'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.creator:
            return True
        return False

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)