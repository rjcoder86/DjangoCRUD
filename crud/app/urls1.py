from django.urls import path, include
from . import views1


urlpatterns = [
    path('', views1.home,name='home'),
    path('empclass1/', views1.EmpClass1.as_view()),
    path('empclass2/<int:pk>/', views1.EmpClass2.as_view()),
]
