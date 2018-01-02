from django.http import HttpResponse
from django.views.generic import ListView
from django.views import View
from django.shortcuts import render
from todos.models import ToDo, List

from datetime import datetime
class ProfileView(ListView):
    model = ToDo 
    context_object_name = "todos"
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['cats'] = List.objects.all()
        return context

class AddTaskView(View):
    def get(self, request):
        todo = ToDo(title=request.GET.get('title'), belong_to=List.objects.get(id=request.GET.get('cat')), due_to=datetime.strptime(request.GET.get('date'),"%m/%d/%Y"), created_by=request.user)
        todo.save();
        return HttpResponse("Success")

class CompleteTaskView(View):
    def get(self, request):
        todo = ToDo.objects.get(id=request.GET.get('task_id'))
        todo.is_completed = True
        todo.save()
        return HttpResponse("Success")


class HomeView(View):
    template_name = "index.html"
    def get(self, request):
        return 	render(request, self.template_name, {})

