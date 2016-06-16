from django import forms
from .models import News
from django.contrib.auth.models import User

class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ('title', 'caption', 'news_text')
        # widgets = {
        #     'title': forms.TextInput(attrs={'size' : 80}),
        #     'caption': forms.TextInput(attrs={'size' : 80}),
        #     'news_text' : forms.Textarea(attrs={'cols' : 80, 'rows' : 20})
        # }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

