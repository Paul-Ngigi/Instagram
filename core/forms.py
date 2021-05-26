from django import forms
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('caption', 'image')
        widgets = {
            'caption': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Caption...'
            })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class UpdateProfile(forms.ModelForm):
      class Meta:
        model = User
        fields = ['bio','profile_image']