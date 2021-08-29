from django import forms


class LoadPriceForm(forms.Form):
    file = forms.FileField()
