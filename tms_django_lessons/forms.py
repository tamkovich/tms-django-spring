from django import forms

class WriteLineForm(forms.Form):
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    age = forms.IntegerField(min_value=0)

class AviaSales(forms.Form):
    name = forms.CharField(max_length=20, required=False)
    whereFrom = forms.CharField(max_length=20, required=False)
    whereTo = forms.CharField(max_length=20, required=False)
    amountPerson = forms.IntegerField(min_value=1)
    date = forms.DateField(required=False)
