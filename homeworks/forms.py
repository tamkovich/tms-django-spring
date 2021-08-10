from django import forms


class TicketOrderForm(forms.Form):
    name = forms.CharField(label='Name', max_length=20, required=True)
    place_from = forms.CharField(label='From', max_length=20, required=True)
    place_to = forms.CharField(label='To', max_length=20, required=True)
    passengers_cnt = forms.IntegerField(label='Amount passengers', min_value=1, required=True)
    flight_date = forms.DateField(label='Flight date', required=True)