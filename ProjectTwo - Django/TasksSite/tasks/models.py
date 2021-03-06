from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Tasks(models.Model):
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    description = models.TextField()
    creator = models.ForeignKey(User, 
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title