from rest_framework import viewsets
from rest_framework.viewsets import ViewSetMixin

from .models import employees
from .serializer import employeeSerializer

class EmpClass1(viewsets.ModelViewSet):
    queryset = employees.objects.all()
    serializer_class = employeeSerializer

class EmpClass3(viewsets.ReadOnlyModelViewSet):
    queryset = employees.objects.all()
    serializer_class = employeeSerializer


class EmpClass2(viewsets.ModelViewSet):
    queryset = employees.objects.all()
    serializer_class = employeeSerializer