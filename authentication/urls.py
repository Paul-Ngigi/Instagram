from django.urls import path
from .views import SignUpView, SignInView, SignOutView
from core.views import home

urlpatterns = [
    path('home/', home, name='home_view'),
    path('signup/', SignUpView.as_view(), name='signup_view'),
    path('', SignInView.as_view(), name='signin_view'),
    path('signout/', SignOutView.as_view(), name='signout_view'),
]
