from .models import CustomUser
from django.forms import ModelForm

class UserCreateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ["firstname", "lastname", "age", "profession"]



