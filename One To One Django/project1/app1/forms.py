from django import forms
from .models import Person, Adhar

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class AdharForm(forms.ModelForm):
    class Meta:
        model = Adhar
        fields = '__all__'

