from django import forms
from .models import Student,Courses

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'

