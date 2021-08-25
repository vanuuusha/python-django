from django import forms
from .models import Comment, News


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description']


class ModerForm(forms.Form):
    CHOICES = [('delete', 'delete'),
               ('publish', 'publish')]

    what_do = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)