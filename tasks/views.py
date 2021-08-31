from django.shortcuts import render
from django.http import HttpResponse


from .models import Task
from .forms import TaskForm
# Create your views here.

def index(request):
    queryset = Task.objects.all()
    form = TaskForm()
    context = {
        'tasks': queryset,
        'form': form,
    }
    return render(request, 'tasks/list.html', context)