from django.shortcuts import render
from .models import PostsModel
from django.views.generic import ListView, DetailView, CreateView

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

# a modelt és a template-et meg kell adni
class PostListView(ListView):
    model = PostsModel
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = PostsModel
    template_name = 'blog/post_detail.html'

class PostCreateView(CreateView):
    model = PostsModel
    template_name = 'blog/post_create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)