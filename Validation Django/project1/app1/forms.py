from django import forms
from django.core import validators

from .models import Registeration
'''
class ElectionForm(forms.Form):
    eid = forms.IntegerField(validators=[validators.MinValueValidator(1)])
    fname = forms.CharField(max_length=40)
    lname = forms.CharField(max_length=40,validators=[validators.MaxLengthValidator(10)])
    mail = forms.EmailField()
    age = forms.IntegerField(validators=[validators.MinValueValidator(1),validators.MaxValueValidator(99)])
    
'''
class RegisterationForm(forms.ModelForm):
    class Meta:
        model = Registeration
        fields = '__all__'


    def clean_eid(self):
        entered_data = self.cleaned_data['eid']
        print('---------',entered_data)

        if entered_data < 1:
            raise forms.ValidationError('EID can not be Zero')
        
        return entered_data
    
    def clean_fname(self):
        entered_data = self.cleaned_data['fname']
        print('------',entered_data)

        if entered_data.istitle():
            raise forms.ValidationError("FIRST LETTER SHOULD BE CAPITAL")
        return entered_data
    
    def clean(self):
        all_data =super().clean()
        password1 = all_data['password']
        password2 = all_data['C_password']
        print(password1,'-------',password2)
        if password1 != password2:
            raise forms.ValidationError('PASSWORD and C_PASSWORD value should be same')
        return all_data
    


    



