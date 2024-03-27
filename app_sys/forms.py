from django import forms
from django.forms import ModelForm
from .models import Note

class AddNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ('title','content')
        labels = {
            'title': '',
            'content': ''
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'content'})
        }