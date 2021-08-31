from django import forms


class AddBlogForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class AddBlogFileForm(forms.Form):
    file = forms.FileField()

