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

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.pk)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def get_user(cls, username):
        profile = cls.objects.filter(user__username__icontains=username)
        return profile


class Comment(models.Model):
    """
    Class that holds comment models
    """
    text = models.CharField(max_length=240)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    comment_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.text)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()


class Like(models.Model):
    """
    Class that holds like models
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    is_like = models.BooleanField(default=True)
    liked_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.is_like)


class Follow(models.Model):
    """
    Class that holds follow models
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow_follower', editable=False)
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow_followed')
    followed_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} --> {self.followed}"
