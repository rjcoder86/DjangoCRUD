from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views3

urlpatterns = [
    path('', views3.home,name='home'),
    path('empclass1/', views3.EmpClass1.as_view()),
    path('empclass2/<int:pk>/', views3.EmpClass2.as_view()),
]

