from django.shortcuts import render
from .views import *

# Create your views here.
from django.views.generic import ListView


def index(request):
    return render(request, 'blog/index.html', context={'range': range(10)})



class Post(ListView):
    model = News