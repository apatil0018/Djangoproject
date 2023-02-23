from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels ={
            'eid':'EMPLOYEE ID',
            'fname': 'FIRST NAME',
            'lname':'LAST NAME',
            'address':'ADDRESS',
            'city': 'CITY',

        }
        widgets = {
            'eid': forms.NumberInput(
            attrs={
            'placeholder':'eg.1',
            'class': 'form-control'
            }

            )
            ,
            'fname':forms.TextInput(
            attrs={
            'placeholder':'eg.Ajit',
            'class': 'form-control'
            }
            )
            ,
            'lname':forms.TextInput(
            attrs={
            'placeholder':'eg.Patil',
            'class': 'form-control'
            }
            )
            ,
            'address': forms.Textarea(
            attrs={
            'placeholder':'eg.KIRTI NAGAR',
            'class':'form-control'
            }
            ),
            'city':forms.TextInput(
            attrs={
            'placeholder':'eg.Nagpur',
            'class': 'form-control'
            }
            )
        }
