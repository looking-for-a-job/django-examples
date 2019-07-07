from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Post

class PostDetailView(DetailView):
    model = Post
    context_object_name = "post" # default is "object"

class PostListView(ListView):
    model = Post
    context_object_name = "post_list" # default is "object_list"
