from django import forms


class UserCreateForm(forms.Form):
    firstname = forms.CharField(max_length=60, required=False)
    lastname = forms.CharField(max_length=60, required=False)
    age = forms.IntegerField(min_value=0, required=False)
    profession = forms.CharField(max_length=50, required=False)
