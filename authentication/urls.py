from django.urls import path
from .views import SignUpView, home


urlpatterns = [
    path('', home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup_view')
]