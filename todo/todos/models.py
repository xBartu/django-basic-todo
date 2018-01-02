from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
class List(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 


class ToDo(models.Model):
    title = models.CharField(max_length=244)
    belong_to = models.ForeignKey(List, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    due_to = models.DateField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 

    def save(self):
        if self.is_completed:
            self.completed_at = datetime.now()
        super(ToDo, self).save()
