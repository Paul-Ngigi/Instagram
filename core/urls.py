from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_view'),
    path('addpost/', views.add_post, name='addpost_view'),
    path('search/', views.search_user, name='search_results'),
    path('profile/', views.profile, name='profile'),
    path('comment/<pk>', views.comment, name='AddComment'),
    path('like/<pk>', views.like, name='like'),
]
