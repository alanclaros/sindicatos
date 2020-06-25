from django.urls import path

from . import views

urlpatterns = [
    path('settings/', views.settings_index, name='settings'),
    path('zonas/', views.zonas_index, name='zonas'),
    path('zonas/add/', views.zona_add, name='zonas_add'),
    path('zonas/<int:zona_id>/change/', views.zona_modify, name='zonas_modify'),
    path('zonas/<int:zona_id>/delete/', views.zona_delete, name='zonas_delete'),

    #path('zonas/<int:zona_id>/', views.zona_modify, name='zona_modify'),
    #path('zonas/<int:zona_id>/', views.zona_delete, name='zona_delete'),

    path('usuarios/', views.zonas_index, name='usuarios'),
    path('cobros_manuales/', views.zonas_index, name='cobros_manuales'),
    path('cobros_mensuales/', views.zonas_index, name='cobros_mensuales'),
]
