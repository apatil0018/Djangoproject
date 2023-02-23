from django.shortcuts import render
from .forms import EmployeeForm
# Create your views here.

def employeeView(request):
    form = EmployeeForm()
    template_name = 'app2/employee.html'
    context = {'form': form}
    return render(request,template_name,context)

