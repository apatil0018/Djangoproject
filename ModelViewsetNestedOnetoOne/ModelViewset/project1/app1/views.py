from django.shortcuts import render
from app1.serializers import EmployeeSerilaizer, AddressSerializer
from app1.models import Employee, AddressDetails
from rest_framework import viewsets


# Create your views here.
class Emp_View(viewsets.ModelViewSet):
    serializer_class = EmployeeSerilaizer
    queryset = Employee.objects.all()


class Add_View(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = AddressDetails.objects.all()


