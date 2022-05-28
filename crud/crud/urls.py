from django.contrib import admin
from django.contrib.sites.requests import RequestSite
from django.shortcuts import render
from django.urls import path, include


def main(request):
    site_name = RequestSite(request).domain
    return render(request,'main.html',{'domain':site_name})

urlpatterns = [
    path('', main),
    path('admin/', admin.site.urls),
    path('apiview/', include('app.urls1')),
    path('mixingeneric/', include('app.urls2')),
    path('generic/', include('app.urls3')),
    path('viewset/', include('app.urls4')),
]