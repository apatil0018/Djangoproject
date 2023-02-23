from app1.models import Student
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    sid=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    FMT=serializers.BooleanField()

    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.sid = validated_data.get('sid',instance.sid)
        instance.name = validated_data.get('name',instance.name)
        instance.FMT = validated_data.get('FMT',instance.FMT)

        instance.save()
        return instance
    
        
    
        
    
    