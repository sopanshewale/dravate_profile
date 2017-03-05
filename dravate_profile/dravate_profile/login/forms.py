from django.contrib.auth.forms import User
from django import forms
from .models import Userprofile


class UserForm(forms.ModelForm):
    class Meta:
         model = User
         fields = ['first_name', 'last_name', 'email']
    def __init__(self, *args, **kwargs):
        return super(UserForm, self).__init__(*args, **kwargs)


class ProfileForm(forms.ModelForm):
    class Meta:
       model = Userprofile
       fields = ['phone', 'address',]
    def __init__(self, *args, **kwargs):
        return super(ProfileForm, self).__init__(*args, **kwargs)



