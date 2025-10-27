from django.db import models
from django.forms import ValidationError

def valida_peso(value):
    if value < 0.01 or value > 200.00:
        raise ValidationError("El peso debe estar entre 10 gramos y 200 kilos")

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    raza = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2, validators=[valida_peso])
    vacunado = models.BooleanField()
    ultima_vacuna = models.DateField(blank=True, null=True)
    email_duenyo = models.EmailField(blank=True)
    domicilio_duenyo = models.CharField(max_length=100, blank=True)

    def clean(self):
        super().clean()
        if self.vacunado == True and not self.ultima_vacuna:
            raise ValidationError({"ultima_vacuna": "Por favor, introduce la fecha de la última vacuna"})
        if self.ultima_vacuna and self.ultima_vacuna < self.fecha_nacimiento:
            raise ValidationError({"ultima_vacuna": "La fecha de la última vacunación debe ser posterior a la fecha de nacimiento"})