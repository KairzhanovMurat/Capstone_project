from django.forms import ModelForm, Form
from . import models
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUp(UserCreationForm):

    class Meta:
        fields = ('username','email','password1', 'password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label='Name'
        self.fields['email'].label = 'email address'
        self.fields['password1'].label = 'password'
        self.fields['password2'].label = 'confirm password'