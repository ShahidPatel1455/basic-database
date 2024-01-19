from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        field = [ 'name' , 'age']
        exclude = []
        # field = ['__all__']