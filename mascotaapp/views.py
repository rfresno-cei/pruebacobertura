from django.http import HttpResponse
from django.shortcuts import render

from mascotaapp.forms import MascotaForm

# Create your views here.
def miform(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Hecho")
    else:
        form = MascotaForm()
    return render(request, "mascotaapp/form.html", {"form": form})