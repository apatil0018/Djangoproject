from django.shortcuts import render
from .forms import StudentForm
# Create your views here.

def StudentView(request):
    form = StudentForm()
    template_name = 'app1/student.html'
    context = {'form': form}
    return render(request,template_name,context)


