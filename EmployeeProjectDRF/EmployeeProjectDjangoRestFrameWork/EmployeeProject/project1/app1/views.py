from rest_framework.response import Response
from django.shortcuts import render
from app1.serializers import EmployeeSerilaizer, AddressSerializer, WorkexpSerializer,QualificationSerializer,ProjectSerializer
from app1.models import Employee, AddressDetails,Workexp,Qualification,Projects
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.
"""
class Emp_View(viewsets.ModelViewSet):
    serializer_class = EmployeeSerilaizer
    queryset = Employee.objects.all()

"""

class EmployeeDetails(APIView):
   # used to Fetch Employee Data 
    def get (self, request):
        try:
            emp = Employee.objects.all()
        except Employee.DoesNotExist:
            msg ={"msg":"Employee Detail not Found", "success":"False", "employee":"[]"}
            return Response(msg, status.HTTP_200_OK)

        serializer = EmployeeSerilaizer(emp, many= True)
        return Response({'msg': "employee details found", "success":"True","employees":serializer.data},status=status.HTTP_200_OK,)

# Used to create/upload data to the server and result in change state of the server.
    def post(self, request):
        serializer = EmployeeSerilaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Employee Created Successfully", "success":"true", "employee":serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class EmployeeInfo(APIView):
    def get(self, request, id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            msg = {'msg':"Employee Does not Exist"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerilaizer(emp)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,id):
        # Used to complete update an alerady existing data.
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            msg = {'msg': 'Employee Does not Exist'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerilaizer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Employee Details Successfully", "success":"True"}, status=status.HTTP_200_OK)
        return Response({'msg':"Invalid Body Request", "success":"False"}, status=status.HTTP_400_BAD_REQUEST)

    
    def patch(self,request,id):
        # Used to  partially update an alerady existing data.
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            msg = {'msg': 'Employee Does not Exist'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerilaizer(emp, data=request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Employee Details Successfully", "success":"True"}, status=status.HTTP_200_OK)
        return Response({'msg':"Invalid Body Request", "success":"False"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,id):
        # Used to delete existing data in the server.
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            msg = {'msg': 'Employee Does not Exist'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        emp.delete()
        return Response({'msg': "employee Delete Successfully", "success": "True"}, status= status.HTTP_204_NO_CONTENT)



    



class Add_View(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = AddressDetails.objects.all()


class Workexp_View(viewsets.ModelViewSet):
    serializer_class = WorkexpSerializer
    queryset = Workexp.objects.all()


class Qualification_View(viewsets.ModelViewSet):
    serializer_class = QualificationSerializer
    queryset = Qualification.objects.all()

class Project_View(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Projects.objects.a

