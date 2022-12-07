from django import forms
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField
from django.shortcuts import redirect

from .models import *

class AddBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = "__all__"

class ContactForm(forms.Form):

    name = forms.CharField(max_length=255, label='Ваше имя')
    last_name = forms.CharField(max_length=255, label='Вашa фамилия')
    email = forms.EmailField(max_length=255, label='Электронный адрес')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}))
    captcha = CaptchaField()

class LoginUserForm(AuthenticationForm):

    username = forms.CharField(label = 'Логин', widget = forms.TextInput(attrs = {'class': 'form-input'}))




