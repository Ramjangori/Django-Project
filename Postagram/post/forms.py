from django import forms
from . models import post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class postform(forms.ModelForm):
    
    class Meta:
        model = post
        fields = ['text' , 'image']
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class meta:
        model = User
        fields = ('username' , 'email' , 'password1' , 'password2')