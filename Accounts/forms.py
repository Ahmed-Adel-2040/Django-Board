from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUp(UserCreationForm):
    email=forms.CharField(max_length=225,required=True,widget=forms.EmailInput)
    First_Name=forms.CharField(max_length=100,required=True)
    Last_Name = forms.CharField(max_length=100, required=True)
    class Mete :
        model=User
        fields={'username','password1','password2','email','First_Name','Last_Name'}