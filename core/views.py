from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment, Like, Follow
from django.contrib.auth import get_user_model
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def home(request):
    posts = Post.objects.all()

    return render(request, 'posts/index.html', {'posts': posts})


@login_required
def add_post(request):
    form = PostCreateForm(request.POST)

    if form.is_valid():
        form.save()
        redirect('home_view')

    else:
        form = PostCreateForm

        return render(request, 'posts/add-post.html', {'form': form})


@login_required
def search_user(request):
    if 'profile' in request.GET and request.GET['profile']:
        search_term = request.GET.get('profile')
        searched_user = Post.get_user(search_term)
        message = f'{searched_user}'

        return render(request, 'all-posts/search.html', {'message': message})

    else:
        message = "We can't seem to find what you are looking for"
        return render(request, 'all-posts/search.html', {'message': message})
