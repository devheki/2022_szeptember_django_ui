from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""
MVC - MVT: Model View Template
"""

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')