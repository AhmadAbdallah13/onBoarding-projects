from django.contrib.auth.models import User
from django.db import models



class Tasks(models.Model):
    title = models.CharField(max_length=100)
    done = models.BooleanField()
    description = models.TextField()
    creator = models.ForeignKey(User, 
                               on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title