from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views4

router=DefaultRouter()
router.register('read_and_create', views4.EmpClass1, basename='EmpClass1')
router.register('read_only', views4.EmpClass3, basename='EmpClass3')
router.register('get_by_id', views4.EmpClass2, basename='EmpClass2')

urlpatterns = [
    path('', include(router.urls)),
]


