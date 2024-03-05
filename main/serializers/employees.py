from rest_framework.serializers import ModelSerializer

from main.models.employees import Employee


class EmployeeSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'
