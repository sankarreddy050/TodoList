from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = "tasks"
    # template_name = "task_list.html" by defalut listview search for template location is this templates/base/task_list.html
class DetailsView(DetailView):
    model = Task
    template_name = "base/task.html"
    context_object_name = "task"
class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")
class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")
class TaskDelete(DeleteView):
    model =Task
    context_object_name = "task"
    success_url = reverse_lazy("tasks")   
    
   
