from django.urls import path
from main.views.employees import EmployeeListGenericAPIView

urlpatterns = [
    path('employee-list', EmployeeListGenericAPIView.as_view(), name='employee_list')
]
