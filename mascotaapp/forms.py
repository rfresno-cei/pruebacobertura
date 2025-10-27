from django import forms

from mascotaapp.models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'
        labels = {
            "fecha_nacimiento": "Fecha de nacimiento",
            "peso": "Peso en kilos",
            "ultima_vacuna": "Fecha de la última vacuna",
            "email_duenyo": "Email del dueño",
            "domicilio_duenyo": "Domicilio del dueño"
        }
        widgets = {
            "fecha_nacimiento": forms.DateInput(attrs={"type": "date"}),
            "ultima_vacuna": forms.DateInput(attrs={"type": "date"})
        }
        error_messages = {
            "nombre": {
                "max_length": "El nombre de la mascota no puede tener más de 20 caracteres",
                "required": "El nombre es obligatorio"
            }
        }