from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from django.urls.base import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView


from .models import Task
from .forms import TaskForm
# Create your views here.


class LandingPageView(generic.TemplateView):
    template_name = 'landing.html'


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('tasks')



def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('.')

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'tasks/list.html', context)

def task_detail(request, pk):
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
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/tasks')

    context = {'item': item}
    return render(request, 'tasks/delete.html', context)