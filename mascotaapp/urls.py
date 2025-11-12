from django.contrib import admin
from django.urls import path

from mascotaapp import views

urlpatterns = [
    path('miform', views.miform, name='miform'),
    path('<int:pk>/edit', views.mascota_edit, name='mascota_edit'),
    path('list', views.mascota_list, name='mascota_list'),
    path('<int:pk>/delete', views.mascota_delete, name='mascota_delete'),
    path('temaoscuro', views.temaoscuro, name='temaoscuro'),
    path('temaamarillo', views.temaamarillo, name='temaamarillo'),
    path('borracookie', views.borracookie, name='borracookie')
]