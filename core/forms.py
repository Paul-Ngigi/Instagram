from django import forms
from .models import Post


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
