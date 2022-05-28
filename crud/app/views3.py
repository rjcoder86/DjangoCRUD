from django.contrib.sites.requests import RequestSite
from django.shortcuts import render
from rest_framework import generics
from .models import employees
from .serializer import employeeSerializer

def home(request):
    site_name = RequestSite(request).domain
    return render(request,'generic.html',{'domain':site_name,'data':employees.objects.all()})

class EmpClass1( generics.ListCreateAPIView):
    queryset = employees.objects.all()
    serializer_class = employeeSerializer

class EmpClass2(generics.RetrieveUpdateDestroyAPIView):
    queryset = employees.objects.all()
    serializer_class = employeeSerializer