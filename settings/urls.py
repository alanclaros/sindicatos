from django.urls import path

from . import views

urlpatterns = [
    path('settings/', views.settings_index, name='settings'),
    path('zonas/', views.zonas_index, name='zonas'),
    path('usuarios/', views.zonas_index, name='usuarios'),
    path('cobros_manuales/', views.zonas_index, name='cobros_manuales'),
    path('cobros_mensuales/', views.zonas_index, name='cobros_mensuales'),
]
