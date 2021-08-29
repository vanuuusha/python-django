from django import forms


class FileForm(forms.Form):
    title = forms.CharField(max_length=20)
    description = forms.CharField(max_length=100)
    file = forms.FileField()


class FileCheckerForm(forms.Form):
    file = forms.FileField()