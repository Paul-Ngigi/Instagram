from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Post, Comment, Like, Follow
from django.contrib.auth import get_user_model
from .forms import PostCreateForm, CommentForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def home(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()

    return render(request, 'posts/index.html', {'posts': posts, 'comments': comments})


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(user=request.user, caption=form.cleaned_data.get('caption'),
                        image=form.cleaned_data.get('image'))
            post.save()
            print(form)

            return redirect('home_view')

    else:
        form = PostCreateForm
        message = f'Error, please try again'

        return render(request, 'posts/add-post.html', {'form': form, 'message': message})


@login_required
def search_user(request):
    if 'profile' in request.GET and request.GET['profile']:
        search_term = request.GET.get('profile')
        searched_user = Post.get_user(search_term)
        print(searched_user)
        message = f'{searched_user}'

        posts = Post.objects.all()
        return render(request, 'posts/search.html', {'message': message, 'posts': searched_user})

    else:
        message = "We can't seem to find what you are looking for"
        return render(request, 'posts/search.html', {'message': message})


@login_required
def profile(request):
    posts = Post.objects.filter(user_id=request.user)

    return render(request, 'posts/profile.html', {"posts": posts})


@login_required
def comment(request, pk):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = Comment(user=request.user,
                              comment=form.cleaned_data.get('text'))
            comment.save()
            comment.user = request.user
            comment.post = post

            return redirect('home_view')
