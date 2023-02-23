from django.shortcuts import render
from .models import Person,Adhar
from .forms import PersonForm, AdharForm

# Create your views here.

def personView(request):
    form = PersonForm()
    template_name = 'app1/person.html'
    context = {'form' : form}

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, template_name, context)

def adharView(request):
    form = AdharForm()
    template_name = 'app1/adhar.html'
    context = {'form': form}

    if request.method == 'POST':
        form =AdharForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, template_name,context)


def showPerson(request):
    obj = Person.objects.all()
    template_name = 'app1/showperson.html'
    context = {'obj':obj}
    return render(request,template_name,context)


def showAdhar(request):
    obj = Adhar.objects.all()
    template_name = 'app1/showadhar.html'
    context = {'obj': obj}
    return render(request,template_name,context)


