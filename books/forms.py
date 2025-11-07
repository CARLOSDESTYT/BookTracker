from django.forms import ModelForm
from django import forms
from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'autor', 'goal', 'pages_read', 'pages_total']
        widgets = {
            'goal': forms.DateInput(attrs={'type': 'date'}),
        }