from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""
MVC - MVT: Model View Template
"""

posts = [
    {
        'author': 'Ricsi Kovács',
        'title': 'Blog post 1',
        'content': 'first content',
        'date_posted': '2022 szeptember 14'
    },
    {
        'author': 'Ricsi Kovács',
        'title': 'Blog post 2',
        'content': 'second content',
        'date_posted': '2022 szeptember 15'
    },
    {
        'author': 'Ricsi Kovács',
        'title': 'Blog post 3',
        'content': '3rd content',
        'date_posted': '2022 szeptember 17'
    },
]


def home(request):
    text = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context=text)

def about(request):
    return render(request, 'blog/about.html')