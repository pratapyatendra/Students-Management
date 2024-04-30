
from rest_framework import serializers
from .models import student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields =('studentsId',
                 'FirstName',
                 'LastName',
                 'RegistrationNo',
                 'Email',
                 'Course')
        
# This is going to convert JSON into Models.💥💥💥
