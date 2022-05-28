from django.contrib.sites.requests import RequestSite
from django.shortcuts import HttpResponse, render
from rest_framework import  mixins,generics
from .models import employees
from .serializer import employeeSerializer

def home(request):
    site_name = RequestSite(request).domain
    return render(request,'mixingeneric.html',{'domain':site_name,'data':employees.objects.all()})

class EmpClass1(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):

    queryset = employees.objects.all()
    serializer_class = employeeSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class EmpClass2(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):

    queryset = employees.objects.all()
    serializer_class = employeeSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*a,**kwargs):
        return self.destroy(request,*a,**kwargs)