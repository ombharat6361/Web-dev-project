from socket import fromshare
from django import forms
from .models import Blog,Room,User
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class BlogForms(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'
        exclude=['user']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude=['host','participants']


# class UserForm(AuthenticationForm):
#     username = UsernameField(widget=forms.TextInput)
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = User
#         fields='__all__'