from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy



class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["author",'title', 'context']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["author",'title', 'context']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    context_object_name = "post"
    success_url = reverse_lazy("home")