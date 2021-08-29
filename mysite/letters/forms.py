from django import forms
from .models import InputLetters


class InputLettersForm(forms.ModelForm):
    class Meta:
        model = InputLetters
        fields = ['letters1', 'letters2', 'letters3']
