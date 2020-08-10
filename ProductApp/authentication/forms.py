from django import forms
from django.core import validators
from django.contrib.auth.models import User

def unique_username(username):
    try:
        User.objects.get(username=username)
        raise forms.ValidationError('Username already exists')
    except User.DoesNotExist:
        return 

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, validators=(unique_username,))
    firstname = forms.CharField()
    lastname = forms.CharField()
    password1 = forms.CharField(min_length=6)
    password2 = forms.CharField()
    email = forms.CharField()

    def clean(self):
        all_cleaned_data = super().clean()
        pwd1 = all_cleaned_data['password1']
        pwd2 = all_cleaned_data['password2']
        if pwd1 != pwd2:
            raise forms.ValidationError('Make sure passwords match')


def userExists(username):
    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
        raise forms.ValidationError('Invalid Credentials')

class LoginForm(forms.Form):
    username = forms.CharField(validators=(userExists,))
    password = forms.CharField()
