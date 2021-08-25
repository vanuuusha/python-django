from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class MyUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    email = forms.EmailField(help_text='Электронная почта', required=True)
    date_of_birth = forms.DateField(required=True, widget=forms.SelectDateWidget(years=[i for i in range(1900, 2010)]))
    city = forms.CharField(max_length=20, required=False)
    card = forms.CharField(max_length=16, required=False)
    telephone = forms.CharField(max_length=10, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_of_birth', 'city', 'card', 'telephone', 'password1', 'password2']