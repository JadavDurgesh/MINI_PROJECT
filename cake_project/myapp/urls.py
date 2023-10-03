"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .import views##
#4 
#5 create folder template, myapp and file index.html
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('registration', views.registration, name='registration'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    
    path('service', views.service, name='service'),
    path('product', views.product, name='product'),
    path('team', views.team, name='team'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('err', views.err, name='err'),
    path('forget_password', views.forget_password, name='forget_password'),
    path('confrom_password', views.confrom_password, name='confrom_password'),


]
