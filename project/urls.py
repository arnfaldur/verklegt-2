"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django.urls
from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path, include


urlpatterns = [
    path('', lambda request: redirect('products/', request)),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('user/', include('user.urls')),
    path('create_product/', include('products.urls')),
    path('delete_product/', include('products.urls')),
    path('update_product/', include('products.urls')),
    path('about/', lambda request: render(request, 'products/about.html')),
    path('contact/', lambda request: render(request, 'products/contact.html')),

]