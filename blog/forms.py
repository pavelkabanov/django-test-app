from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
    title = forms.CharField(max_length=200, label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control'}))

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email',)
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}))

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
