from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from mascotaapp import views

urlpatterns = [
    path('miform', views.miform, name='miform'),
    path('<int:pk>/edit', views.mascota_edit, name='mascota_edit'),
    path('list', views.MascotaList.as_view(), name='mascota_list'),
    path('<int:pk>/delete', views.mascota_delete, name='mascota_delete'),
    path('temaoscuro', views.temaoscuro, name='temaoscuro'),
    path('temaamarillo', views.temaamarillo, name='temaamarillo'),
    path('borracookie', views.borracookie, name='borracookie'),
    path('<int:pk>/detail', views.MascotaDetail.as_view(), name='detail'),
    path('registro', views.registro, name='registro'),
    path('login', LoginView.as_view(template_name = 'mascotaapp/form.html', redirect_authenticated_user = True), name='login'),
    path('logout', LogoutView.as_view(), name='logout')
]