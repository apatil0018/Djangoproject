from django import forms
from .models import Orders

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
        labels = {
            'o_id': 'ORDER ID',
            'f_name': 'FIRST NAME',
            'l_name' : 'LAST NAME',
            'amt':'AMOUNT',
            'mail': 'MAIL ID',
            'address': 'ADDRESS'
        }
        widgets = {
            'o_id': forms.NumberInput(
            attrs={
            'placeholder':'eg.1'
            }
            ),
            'f_name':forms.TextInput(
            attrs={
            'placeholder': 'eg.Ajit'
            }
            ),
            'l_name':forms.TextInput(
            attrs={
            'placeholder':'eg.Patil'
            }
            ),
            'amt':forms.NumberInput(
            attrs={
            'placeholder':'eg.45000'
            }
            ),
            'mail':forms.EmailInput(
            attrs={
            'placeholder':'eg.apatil0018@gmail.com'
            }
            ),
            'address': forms.Textarea(
            attrs={
            'placeholder':'eg.Karve Nagar,Pune 440058'
            }
            )
            
        
        }

    

    


        