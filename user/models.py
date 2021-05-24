from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class User(AbstractUser):
    picture = CloudinaryField('profile_pictures')
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    objects = BaseUserManager()
