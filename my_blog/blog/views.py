from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""
MVC - MVT: Model View Template
"""

def home(request):
    return HttpResponse('<h1>Blog home valami </h1>')

def about(request):
    return HttpResponse('<h1>About page</h1>')