from django.urls import path
from .views import SignUpView, home, SignInView


urlpatterns = [
    path('', home, name='home_view'),
    path('signup/', SignUpView.as_view(), name='signup_view'),
    path('signin/', SignInView.as_view(), name='signin_view')
]