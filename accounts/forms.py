from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from .models import CustomUser

# SignupForm
class UserSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_picture', 'password1', 'password2', 'address_line1', 'city', 'state', 'pincode', 'is_patient', 'is_doctor']
    
    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'username',
            'first_name',
            'last_name',
            'email',
            'profile_picture',
            'password1',
            'password2',
            'address_line1',
            'city',
            'state',
            'pincode',
            'is_patient',
            'is_doctor',
            ButtonHolder(
                Submit('submit', 'Sign Up', css_class='btn btn-primary')
            )
        )
