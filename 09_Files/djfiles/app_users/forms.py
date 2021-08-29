from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    login = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)


class CreateUserForm(UserCreationForm):
    telephone = forms.CharField(max_length=12, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'telephone', 'password1', 'password2')


class AccountRadactForm(forms.ModelForm):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    telephone = forms.CharField(max_length=12, required=True)

    def save(self, *args, **kwargs):
        super(AccountRadactForm, self).save(*args, **kwargs)
        self.instance.profile.telephone = self.cleaned_data.get('telephone')
        self.instance.profile.save()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'telephone')