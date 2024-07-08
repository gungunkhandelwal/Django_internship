from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import *

class UserSignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    profile_picture=forms.ImageField()
    email=forms.EmailField()
    address_line1 = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    pincode = forms.CharField(max_length=10)

    class Meta:
        model=CustomUser
        fields=['username','first_name','last_name','email','profile_picture', 'password1', 'password2', 'address_line1', 'city', 'state', 'pincode', 'is_patient', 'is_doctor']

    


