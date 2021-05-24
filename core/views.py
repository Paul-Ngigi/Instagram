from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def home(request):
    template_name = 'index.html'
    posts = Post.objects.all()
    return render(request, template_name, {'posts': posts})
