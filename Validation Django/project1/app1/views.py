from django.shortcuts import render,HttpResponse
#from .forms importRegisterationForm
from .forms import RegisterationForm

# Create your views here.

def electionView(request):
    form =RegisterationForm()
    template_name = 'app1/election.html'
    context = {'form': form}
    if request.method == 'POST':
        form =RegisterationForm(request.POST)
        if form.is_valid():
            return HttpResponse('<h1 style="color:green;">Data is Valid</h1>')
       # else:
           # return HttpResponse('<h1 style= "color:red;">Data is invalid</h1>')
    context ={'form':form}   
    return render(request,template_name,context)


