from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment, Like, Follow
from django.contrib.auth import get_user_model
from django.views.generic import View
from .forms import PostCreateForm


# Create your views here.
class Home(View):
    template_name = 'posts/index.html'

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context = {'posts': posts}

        return render(request, self.template_name, context)
    
class AddPost(View):
    template_name = 'posts/add-post.html'
    form = PostCreateForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}

        return render(request, self.template_name, context)
