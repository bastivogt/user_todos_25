from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",

            "email",
            "password1",
            "password2"
        ]
        

class SignInForm(AuthenticationForm):
    pass