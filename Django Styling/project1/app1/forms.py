from django import forms

class StudentForm(forms.Form):
    rn = forms.IntegerField(label="ROLL",widget=forms.NumberInput(attrs={'placeholder':'eg.1','class':'form-control'}))
    fname = forms.CharField(max_length=100,label='FIRST NAME',widget=forms.TextInput(attrs={'placeholder':'eg.Ajit','class':'form-control'}))
    lname = forms.CharField(max_length=100,label='LAST NAME',widget=forms.TextInput(attrs={'placeholder':'eg.Patil','class':'form-control'}))
    mail = forms.EmailField(label='E-MAIL',widget=forms.EmailInput(attrs={'placeholder':'eg.apatil0018@gmail.com','class':'form-control'}))
    password = forms.CharField(max_length=40,label='PASSWORD',widget=forms.PasswordInput(attrs={'placeholder':'eg.Ajit@123','class':'form-control'}))
    C_password = forms.CharField(max_length=40,label='CONFIRM PASSWORD',widget=forms.PasswordInput(attrs={'placeholder':'eg.Ajit@123','class':'form-control'}))

