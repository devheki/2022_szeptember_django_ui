from django.shortcuts import render
from .models import PostsModel

# Create your views here.
"""
MVC - MVT: Model View Template
"""

def home(request):
    posts = PostsModel.objects.all()
    text = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context=text)

def about(request):
    return render(request, 'blog/about.html')