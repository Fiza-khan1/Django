# Import necessary modules
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Define your custom forms here

class SignUpForm(UserCreationForm):
    password2=forms.CharField(label='Password Again',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels={'username':'User Name','first_name':'First Name','last_name':'Last Name','email':'Email'}

# You can define more forms here if needed for your application




