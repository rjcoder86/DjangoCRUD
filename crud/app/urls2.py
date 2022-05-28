from django.urls import path
from . import views2

urlpatterns = [
    path('', views2.home,name='home'),
    path('empclass1/', views2.EmpClass1.as_view()),
    path('empclass2/<int:pk>/', views2.EmpClass2.as_view()),
]
