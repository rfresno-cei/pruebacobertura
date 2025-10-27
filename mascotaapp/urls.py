from django.contrib import admin
from django.urls import path

from mascotaapp import views

urlpatterns = [
    path('miform', views.miform, name='miform'),
]