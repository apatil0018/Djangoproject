from rest_framework import serializers
from app1.models import Employee, AddressDetails


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressDetails
        fields = '__all__'

class EmployeeSerilaizer(serializers.ModelSerializer):
    addressDetails = AddressSerializer(read_only =True)
    class Meta:
        model = Employee
        fields = '__all__'








