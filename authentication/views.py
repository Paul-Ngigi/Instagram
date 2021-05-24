from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import View
from .forms import UserForm, CustomUserChangeForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages

# Create your views here.
User = get_user_model()

class SignUpView(View):
    template_name = 'signup.html'
    user_form = UserForm
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_view')
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        form = self.user_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin_view')
        
        return render(request, self.template_name, {'form': form})
    


class SignInView(View):
    template_name = 'signin.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_view')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email_username = request.POST.get('email_username')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(username=email_username)
            email = user_obj.email
        except Exception as e:
            email = email_username

        user = authenticate(request, email=email, password=password)
        
        if user is None:
            messages.error(request, 'Invalid Login.', extra_tags="error")
            return render(request, self.template_name) 

        login(request, user)
        messages.success(request, 'Thanks for Login, Welcome to Instagram.', extra_tags='success')
        return redirect('home_view')
        
