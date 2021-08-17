from django import forms


class UserForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=20)
    password = forms.CharField(min_length=4, max_length=20)
    first_name = forms.CharField(min_length=3, max_length=20)