from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import View
from .forms import UserForm, CustomUserChangeForm

# Create your views here.
def home(request):
    return HttpResponse('Home')


class SignUpView(View):
    template_name = 'signup.html'
    user_form = UserForm
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        form = self.user_form(request.POST)
        breakpoint()
        if form.is_valid():
            form.save()
            return redirect('home')
        
        return render(request, self.template_name, {'form': form})
