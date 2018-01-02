from django.contrib import admin
from todos.models import ToDo, List

admin.site.register(List)
admin.site.register(ToDo)
