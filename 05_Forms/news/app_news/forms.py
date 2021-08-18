from django import forms
from .models import News, Comment
from django.core.exceptions import ValidationError


class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']

    def clean_author(self):
        author = self.cleaned_data['author']
        if author == 'aaaa':
            raise ValidationError('Автор не подходит')

        return author