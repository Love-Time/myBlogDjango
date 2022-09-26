from django.shortcuts import render
from .models import *

# Create your views here.
from django.views.generic import ListView


def index(request):
    return render(request, 'blog/index.html', context={'range': range(10)})


class Posts(ListView):
    model = News
    template_name = 'blog/news.html'
    context_object_name = "posts"

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class Posts_Category(ListView):
    model = News
    template_name = 'blog/news.html'
    paginate_by = 6

    def get_queryset(self):
        return News.objects.filter(is_published=True, category_id=self.kwargs['category_id'])
