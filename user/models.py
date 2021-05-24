from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from .managers import CustomUserManager


# Create your models here.
class User(AbstractUser):
    picture = CloudinaryField('profile_pictures', null=False, blank=False)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
