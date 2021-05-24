from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.views.generic.edit import UpdateView

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','password1','password2']


class automarksmsForm(forms.Form):
    description = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Enter a brief description'}))
    message = forms.CharField(max_length=320,
                widget=forms.Textarea(attrs={'placeholder': 'Enter your message here. Opt out is considered as 16 characters.',
                'onkeyup':'return charcountupdate(this.value);'}))

class autofastsmsForm(forms.Form):
    description = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Enter a brief description'}))
    message = forms.CharField(max_length=320,
                widget=forms.Textarea(attrs={'placeholder': 'Enter your message here. Opt out is considered as 16 characters.',
                'onkeyup':'return charcountupdate(this.value);'}))

class winpartsmsForm(forms.Form):
    description = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Enter a brief description'}))
    message = forms.CharField(max_length=320,
                widget=forms.Textarea(attrs={'placeholder': 'Enter your message here. Opt out is considered as 16 characters.',
                'onkeyup':'return charcountupdate(this.value);'}))
    
class autofasttotalForm(forms.Form):
    description = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Enter a brief description'}))
    message = forms.CharField(max_length=320,
                widget=forms.Textarea(attrs={'placeholder': 'Enter your message here. Opt out is considered as 16 characters.',
                'onkeyup':'return charcountupdate(this.value);'}))

class corpsmsForm(forms.Form):
    description = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Enter a brief description'}))
    message = forms.CharField(max_length=320,
                widget=forms.Textarea(attrs={'placeholder': 'Enter your message here. Opt out is considered as 16 characters.',
                'onkeyup':'return charcountupdate(this.value);'}))



   
