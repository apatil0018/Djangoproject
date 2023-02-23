from django.shortcuts import render,redirect
from .forms import OrdersForm
from .models import Orders
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def orderFormView(request):
    form = OrdersForm()
    template_name = 'app1/order_form.html'
    context = {'form': form}
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showorder_url')

    return render(request,template_name,context)

@login_required()
def showOrdersView(request):
    obj = Orders.objects.all()
    template_name = 'app1/show_orders.html'
    context = {'obj':obj}
    return render(request,template_name,context)


def updateOrdersView(request,id):
    obj = Orders.objects.get(o_id=id)
    #print(type(obj),obj)
    form = OrdersForm(instance=obj)
    template_name = 'app1/order_form.html'
    if request.method == 'POST':
        form = OrdersForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showorder_url')
    context = {'form': form}
    return render(request,template_name,context)


def deleteOrderView(request,id):
    obj = Orders.objects.get(o_id=id)
    template_name = 'app1/confirmation.html'
    context = {'obj':obj}
    if request.method == 'POST':
        obj.delete()
        return redirect('showorder_url')
    
    return render(request,template_name,context)













