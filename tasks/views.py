from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from django.urls.base import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm

from .models import Task
from .forms import TaskForm


class LandingPageView(generic.TemplateView):
    template_name = 'landing.html'


class CustomSignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm

    def get_success_url(self) -> str:
        return reverse('login-page')


def index(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    tasks = Task.objects.all()
    form = TaskForm()
    user = request.user

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)

            obj.user = user

            obj.save()

        return redirect('.')

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'tasks/list.html', context)

def task_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('/login')
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/tasks')

    context = {'form': form}

    return render(request, 'tasks/detail.html', context)

def task_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/login')
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/tasks')

    context = {'item': item}
    return render(request, 'tasks/delete.html', context)