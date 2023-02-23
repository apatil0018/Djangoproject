from django.shortcuts import render,redirect
from .forms import StudentForm, CoursesForm
from .models import Student,Courses

# Create your views here.
def studentView(request):
    form = StudentForm()
    template_name = 'app1/studentform.html'
    context = {'form': form}

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentdataurl')

    return render(request,template_name,context)


def coursesView(request):
    form = CoursesForm()
    template_name = 'app1/coursesform.html'
    context = {'form': form}

    if request.method =='POST':
        form = CoursesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coursedataurl')
    return render(request,template_name,context)


def showStudent(request):
    obj = Student.objects.all()
    template_name = 'app1/showstudent.html'
    context = {'obj': obj}
    return render(request,template_name,context)

def showCourses(request):
    obj = Courses.objects.all()
    template_name = 'app1/showcourses.html'
    context = {'obj': obj}
    return render(request,template_name,context)




