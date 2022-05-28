from django.contrib.sites.requests import RequestSite
from django.shortcuts import render, HttpResponse
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import generics
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import employees
from .serializer import employeeSerializer

def home(request):
    site_name = RequestSite(request).domain
    return render(request,'apiview.html',{'domain':site_name,'data':employees.objects.all()})

class EmpClass1( APIView):
    def get(self,request,format=None):
        emp=employees.objects.all()
        empserl=employeeSerializer(emp,many=True)
        return Response(empserl.data)

    def post(self,request,format=None):
        empserl=employeeSerializer(data=request.data)
        if empserl.is_valid():
            empserl.save()
            return Response(empserl.data,status=status.HTTP_201_CREATED)
        return Response(empserl.errors,status=status.HTTP_400_BAD_REQUEST)

class EmpClass2(APIView):
    def get_obj(self,pk):
        try:
            return (employees.objects.get(empid=pk))
        except employees.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        emp=self.get_obj(pk)
        empserl=employeeSerializer(emp)
        return Response(empserl.data)

    def put(self,request,pk,format=None):
        emp=self.get_obj(pk)
        empserl=employeeSerializer(emp,data=request.data)
        if empserl.is_valid():
            empserl.save()
            return Response(empserl.data,status=status.HTTP_201_CREATED)
        return Response(empserl.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        emp=self.get_obj(pk)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
