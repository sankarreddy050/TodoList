from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from .models import Task

# Create your views here.
class CustomLoginView(LoginView):
    template_name = "base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy("tasks")
class Logout(LogoutView):
    next_page = "login"
class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = "tasks"
    # template_name = "task_list.html" by defalut listview search for template location is this templates/base/task_list.html
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count']= context['tasks'].filter(complete=False).count()
        return context
class DetailsView(LoginRequiredMixin,DetailView):
    model = Task
    template_name = "base/task.html"
    context_object_name = "task"
class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy("tasks")
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)
    
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")
class TaskDelete(LoginRequiredMixin,DeleteView):
    model =Task
    context_object_name = "task"
    success_url = reverse_lazy("tasks")   
    
   
