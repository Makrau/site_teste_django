from django import forms
from .models import News, Comment
from django.contrib.auth.models import User

class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ('title', 'caption', 'news_text', 'news_type')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'comment_text')

