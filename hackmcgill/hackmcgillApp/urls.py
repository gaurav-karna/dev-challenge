from django.urls import path, include
# from django.contrib import admin
from . import views
# import django.contrib.auth
# from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('success', views.success, name='success'),

    path('portal/', include('django.contrib.auth.urls')),
    # logged in
    path('portal/login/diverge', views.diverge, name='diverge'),
    path('portal/login/admin_home', views.admin_home, name='admin_home'),
    path('portal/login/create_admin', views.create_admin, name='create_admin'),
    # logout protocol
    path('', views.logout_screen, name='logout_screen'),

]