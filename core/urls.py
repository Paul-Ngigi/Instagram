from django.urls import path
from .views import Home, AddPost

urlpatterns = [
    path('', Home.as_view(), name='home_view'),
    path('addpost/', AddPost.as_view(), name='addpost_view'),
]