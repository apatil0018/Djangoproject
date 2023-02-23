from django.shortcuts import render
from rest_framework import generics
from .serializers import CompanySerializer, WorkexpSerializer,QualificationSerializer,ProjectSerializer
from .models import Company,Workexp,Qualification,Projects

# Create your views here.

class CompanyListView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

class WorkexpListView(generics.ListCreateAPIView):
    serializer_class = WorkexpSerializer
    queryset = Workexp.objects.all()


class QualificationListView(generics.ListCreateAPIView):
    serializer_class = QualificationSerializer
    queryset = Qualification.objects.all()

class ProjectListView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Projects.objects.all()
    

