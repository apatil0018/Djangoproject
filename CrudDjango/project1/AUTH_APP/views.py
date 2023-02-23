from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def registerView(request):
    form = UserCreationForm()
    template_name = 'AUTH_APP/register.html'
    context = {'form': form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showorder_url')

    return render(request,template_name,context)


def loginView(request):
    template_name = 'AUTH_APP/login.html'
    context = {}
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        
        user = authenticate(username=un,password=pw)
        print('user value is:------',user)
        
        if user is not None:
            login(request,user)
            return redirect('addorder_url')
        

    return render(request,template_name,context)

def logoutView(request):
    logout(request)
    return redirect('login_url')

