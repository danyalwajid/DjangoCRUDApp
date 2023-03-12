from rest_framework import serializers
from .models import Student

class StudentSeralizer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    
    def create(self , validate_data):
        return Student.objects.create(**validate_data)
    
    def update(self, instance , validate_data):
        instance.name = validate_data.get("name", None) 
        instance.roll = validate_data.get("roll", None) 
        instance.city = validate_data.get("city", None) 
        instance.save()
        return instance
    
    # Field validation 
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return va
    
    def validate(self, data):
        name = data.get("name")
        city = data.get("city")
        if name.lower() == 'rohit' and city.lower() != 'Islamabad':
            raise serializers.ValidationError("Must Enter Valid Values")
        return data 