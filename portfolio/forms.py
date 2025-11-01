from django import forms
from .models import Message

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'text']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'border border-gray-300 p-3 rounded w-full',
                'placeholder': 'Ваше имя'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'border border-gray-300 p-3 rounded w-full',
                'placeholder': 'Ваш email'
            }),
            'text': forms.Textarea(attrs={
                'class': 'border border-gray-300 p-3 rounded w-full h-32',
                'placeholder': 'Ваше сообщение...'
            }),
        }
