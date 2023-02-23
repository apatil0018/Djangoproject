from django.shortcuts import render
from .forms import StudentForm
from .models import StudentRecord
from .utils import render_to_pdf, download_to_pdf


# Create your views here.

def stuView(request):
    form = StudentForm()
    template_name = 'app1/student.html'
    context = {'form': form}
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request,template_name,context)


def ResultList(request,roll_no):
    template_name = "app1/pdf.html"
    records = StudentRecord.objects.all().order_by("roll_no")


    if roll_no==1:
        return render_to_pdf(
            template_name,{
                "record": records
        },
    )


    elif roll_no ==2:
        return download_to_pdf(
            template_name,{
                "record": records,
        },
    )    



    




    

