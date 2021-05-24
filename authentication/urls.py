from django.urls import path
from .views import SignUpView, SignInView, SignOutView
from core.views import Home

urlpatterns = [
    path('home/', Home.as_view(), name='home_view'),
    path('signup/', SignUpView.as_view(), name='signup_view'),
    path('', SignInView.as_view(), name='signin_view'),
    path('signout/', SignOutView.as_view(), name='signout_view'),
]
