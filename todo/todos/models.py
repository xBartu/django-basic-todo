from django.db import models
from django.contrib.auth import User
from datetime import datetime
class List(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

    class Meta:
        ordering = ["name"]

class ToDo(models.Model):
    title = models.CharField(max_length=244)
    _list = models.ForeignKey(List)
    created_at = models.DateField(auto_now=True)
    due_to = models.DateField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(User)
    note = models.TextField()

    def __str__(self):
        return self.title 

    def save(self):
        if is_completed:
            self.completed_at = datetime.now()
        super(ToDo).save()

    class Meta:
        ordering = ["due_to"]

