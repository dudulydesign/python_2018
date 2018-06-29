from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
  username = forms.CharField(min_length=3)
  password = forms.CharField(widget=forms.PasswordInput)

  
