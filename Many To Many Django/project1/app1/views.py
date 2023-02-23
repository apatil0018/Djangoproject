from django.shortcuts import render,redirect
from .forms import Ownersform,CarsForm
from .models import Owners,Cars

# Create your views here.

def ownerView(request):
    form = Ownersform()
    template_name = 'app1/owner.html'
    context = {"form": form}
    if request.method == "POST":
        form = Ownersform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_own_url')

    return render(request,template_name,context)


def carView(request):
    form = CarsForm()
    template_name = 'app1/car.html'
    context = {"form":form}
    if request.method == 'POST':
        form = CarsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_car_url')
        

    return render(request,template_name,context) 


def showownView(request):
    obj = Owners.objects.all()
    template_name = 'app1/show_owner.html'
    context = {'obj': obj}
    return render(request,template_name,context)

def showcarView(request):
    obj = Cars.objects.all()
    template_name = 'app1/show_car.html'
    context = {'obj': obj}
    return render(request,template_name,context)


def updateownView(request,id):
    obj = Owners.objects.get(oid=id)
    form =Ownersform(instance=obj)
    template_name = 'app1/owner.html'
    if request.method == 'POST':
        form = Ownersform(request.POST,instance=obj)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request,template_name,context)

def updatecarView(request,id):
    obj = Cars.objects.get(id=id)
    form = CarsForm(instance=obj)
    template_name ='app1/car.html'
    if request.method == 'POST':
        form =CarsForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request,template_name,context)

def deleteownView(request,id):
    obj = Owners.objects.get(oid=id)
    template_name ='app1/confirmation.html'
    context = {'obj':obj}
    if request.method == 'POST':
        obj.delete()
        return redirect('show_own_url')

    return render(request,template_name,context)


def deletecarView(request,id):
    obj = Cars.objects.get(id=id)
    template_name = 'app1/confirm.html'
    context = {'obj':obj}
    if request.method == 'POST':
        obj.delete()
        return redirect('show_car_url')
    

    return render(request,template_name,context)












