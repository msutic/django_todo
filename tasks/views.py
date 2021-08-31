from django.shortcuts import render
from django.http import HttpResponse

from .models import Task
# Create your views here.

def index(request):
    queryset = Task.objects.all()
    context = {
        'tasks': queryset,
    }
    return render(request, 'tasks/list.html', context)