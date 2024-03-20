from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm

from django.forms.widgets import PasswordInput, TextInput

from . models import profile

from django import forms

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email','password1','password2')


class LoginFrom(AuthenticationForm):
    username = forms.CharField(widget=TextInput()),
    password= forms.CharField(widget=PasswordInput()),

class UpdateUserForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ('username','email')
        

class UpdateProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))

    class Meta:
            model = profile
            fields =['profile_pic']

