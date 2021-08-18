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

    # def clean_author(self):
    #     author = self.cleaned_data['author']
    #     if author == 'aaaa':
    #         raise ValidationError('Автор не подходит')
    # TODO Метод должен вернуть "ощищенные" данные:
    #  https://docs.djangoproject.com/en/3.2/ref/forms/validation/#cleaning-a-specific-field-attribute