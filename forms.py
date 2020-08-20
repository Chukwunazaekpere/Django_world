from django import forms

from allauth.account.forms import SignupForm as BaseSignupForm

from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User
from allauth.account.adapter import get_adapter


class SignupForm(BaseSignupForm):

    def save(self, request):
        user          = User()
        user.email    = request.POST['email']
        user.password = request.POST['password1']

        user.save()
        return user


class ChangeUserDetails(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        Model = User
        exclude = ['created']

    def clean_password(self):
        return self.initial.get('password')
