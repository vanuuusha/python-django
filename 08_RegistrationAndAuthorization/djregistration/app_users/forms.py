from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class PhoneWidget(forms.MultiWidget):
    def __init__(self, code_length=3, num_length=7, attrs=None):
        widgets = [
            forms.TextInput(attrs={'size': code_length, 'maxlength': code_length}),
            forms.TextInput(attrs={'size': num_length, 'maxlength': num_length})
        ]
        super(PhoneWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.code, value.number]
        return ['', '']

    def format_output(self, rendered_widgets):
        return '+7' + '(' + rendered_widgets[0] + ') - ' + rendered_widgets[1]


class PhoneField(forms.MultiValueField):
    def __init__(self, code_length, num_length, *args, **kwargs):
        list_fields = [forms.CharField(),
                       forms.CharField()]
        super(PhoneField, self).__init__(list_fields, widget=PhoneWidget(code_length, num_length), *args, **kwargs)

    def compress(self, values):
        return ''.join(['+7', values[0], values[1]])


class RegisterForm(UserCreationForm):
    telephone = PhoneField(code_length=3, num_length=7)
    city = forms.CharField(max_length=15, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'telephone', 'city']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
