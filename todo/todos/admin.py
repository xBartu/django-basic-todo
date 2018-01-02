from django.contrib import admin
from todos.models import ToDos, List

class ToDosAdmin(admin.ModelAdmin):
    list_display = ('title', 'list', 'due_to')
    ordering = ('due_to')

admin.site.register(List)
admin.site.register(Todos, ToDosAdmin)
