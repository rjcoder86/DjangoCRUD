from rest_framework import serializers
from .models import employees


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=employees
        fields='__all__'

# class departmentSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model=department
#         fields='__all__'