from django import forms
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



