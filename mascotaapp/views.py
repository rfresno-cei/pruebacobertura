from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from mascotaapp.forms import MascotaForm
from mascotaapp.models import Mascota

# Create your views here.
def miform(request):
    tema = request.COOKIES.get('tema', 'nada')
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Hecho")
    else:
        form = MascotaForm()
    return render(request, "mascotaapp/form.html", {"form": form, "tema": tema})

def mascota_edit(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES, instance=mascota)
        if form.is_valid():
            form.save()
            return HttpResponse("Hecho")
    else:
        form = MascotaForm(instance=mascota)
    return render(request, "mascotaapp/form.html", {"form": form})

def mascota_list(request):
    tema = request.COOKIES.get('tema', 'nada')
    mascotas = Mascota.objects.all()
    return render(request, 'mascotaapp/list.html', {'mascotas': mascotas, 'tema': tema})

def mascota_delete(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota_list')
    return render(request, 'mascotaapp/confirm_delete.html', {})

def crea_cookie(request):
    resp = redirect('mascota_list')
    resp.set_cookie('tema', 'oscuro')
    return resp

def lee_cookie(request):
    tema = request.COOKIES.get('tema', 'nada')
    return HttpResponse(f'Tema actual: {tema}')

def borra_cookie(request):
    resp = redirect('mascota_list')
    resp.delete_cookie('tema')
    return resp

def temaoscuro(request):
    resp = redirect('miform')
    resp.set_cookie('tema', 'oscuro')
    return resp

def temaamarillo(request):
    resp = redirect('miform')
    resp.set_cookie('tema', 'amarillo')
    return resp

def borracookie(request):
    resp = redirect('miform')
    resp.delete_cookie('tema')
    return resp