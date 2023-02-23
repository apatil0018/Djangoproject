from django import forms
from .models import Owners,Cars

class Ownersform(forms.ModelForm):
    class Meta:
        model = Owners
        fields = '__all__'


class CarsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = "__all__"

        