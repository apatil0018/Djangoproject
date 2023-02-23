from drf_extra_fields.fields import Base64ImageField
from .models import Company,Workexp,Qualification,Projects
from rest_framework import serializers

class WorkexpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workexp
        fields = '__all__'


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'  


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    workexp = WorkexpSerializer(many=True, read_only=True)
    qualifications = QualificationSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    class Meta:
        model = Company
        fields = '__all__'
        