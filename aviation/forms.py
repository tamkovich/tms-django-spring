from django import forms
from django.forms import SelectDateWidget


class AviationCreateForm(forms.Form):
    Имя_пассажира = forms.CharField(max_length=50, required=True)
    Откуда_летим = forms.CharField(max_length=30, required=True)
    Куда_летим = forms.CharField(max_length=30, required=True)
    Сколько_человек = forms.IntegerField(min_value=1, required=True)
    Дата_вылета = forms.DateField(widget=SelectDateWidget, required=True)
