from django import forms


class WriteLineForm(forms.Form):
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    age = forms.IntegerField(min_value=0, max_value=99)


class AviaSales(forms.Form):
    name = forms.CharField(max_length=20)
    where = forms.CharField(max_length=20)
    To = forms.CharField(max_length=20)
    amountPerson = forms.IntegerField(min_value=1)
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))