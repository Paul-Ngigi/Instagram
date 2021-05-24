from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
def home(request):
    pass


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        title = 'Register'
        return render(request, 'signup.html', {'title': title})
    
    def post(self, request, *args, **kwargs):
        pass
