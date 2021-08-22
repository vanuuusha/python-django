from django import forms


class AuthForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
