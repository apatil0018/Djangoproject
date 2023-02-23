from rest_framework import serializers
from app1.models import Employee, AddressDetails, Workexp,Qualification,Projects

from drf_extra_fields.fields import Base64ImageField


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressDetails
        fields = '__all__'


class WorkexpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workexp
        exclude = ( 'id',) 


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        exclude = ( 'id',)  


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        exclude = ('id',)


class EmployeeSerilaizer(serializers.ModelSerializer):
    photo = Base64ImageField()
    addressDetails = AddressSerializer(read_only =True)
    workexp = WorkexpSerializer(many=True, read_only=True)
    qualifications = QualificationSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    class Meta:
        model = Employee
        fields =  ['name', 'email', 'age', 'gender', 'phoneNo', 'addressDetails', 'workexp','qualifications', 'projects', 'photo' ]

