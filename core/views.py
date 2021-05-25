from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Post, Comment, Like, Follow
from django.contrib.auth import get_user_model
from django.views.generic import View
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def home(request):
    posts = Post.objects.all()
    
    return render(request, 'posts/index.html', {'posts': posts})