from django import forms
from django.contrib.auth.models import User
from .models import User  # Assuming you have a custom User model

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','mobile' ,'name','profile','password', 'email', 'department', 'role')
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)