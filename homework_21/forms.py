from django import forms


class UserEditForm(forms.Form):
    firstname = forms.CharField(label='Firstname', max_length=50)
    lastname = forms.CharField(label='Lastname', max_length=50)
    age = forms.IntegerField(label='Age')
    profession = forms.CharField(label='Profession', max_length=100)