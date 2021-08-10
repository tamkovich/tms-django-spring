from django.forms import ModelForm, TextInput, NumberInput
import MyHW.models


class CRUDuser(ModelForm):
    class Meta:
        model = MyHW.models.User
        fields = ['firstname', 'lastname', 'age', 'profession']
        widgets = {'firstname': TextInput(attrs={
            'placeholder': 'Firstname'}),
            'lastname': TextInput(attrs={
                'placeholder': 'Lastname'}),
            'age': NumberInput(attrs={
                'placeholder': 'Age'}),
            'profession': TextInput(attrs={
                'placeholder': 'Profession'}),
        }