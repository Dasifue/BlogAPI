from .models import Tag, Post
from django import forms 


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('id', 'author')

class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        exclude = ('id',)

