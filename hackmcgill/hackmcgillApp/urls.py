from django.urls import path, include
# from django.contrib import admin
from . import views
# import django.contrib.auth
# from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('success', views.success, name='success'),

]