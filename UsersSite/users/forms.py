from .models import CustomUser
from django.forms import ModelForm
from django import forms


class UserCreateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ["firstname", "lastname", "age", "profession"]


class UserUpdateForm(forms.Form):
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    age = forms.IntegerField()
    profession = forms.CharField(max_length=50)



