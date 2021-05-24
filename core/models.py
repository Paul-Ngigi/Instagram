from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Post(models.Model):
    """
    Class that holds post models
    """
    image = CloudinaryField('post')
    caption = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image
