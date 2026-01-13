from datetime import date
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from mascotaapp.models import Duenyo, Mascota

# Create your tests here.
class MascotaTest(TestCase):
    def test_correct_mascota(self):
        mascota = Mascota.objects.create(
            nombre = 'Trueno',
            raza = 'Pitbull',
            fecha_nacimiento = date(2008, 5, 12),
            peso = 12,
            vacunado = False,
            tipo = 'PE'
        )
        mascota.full_clean()
        self.assertEqual(mascota.nombre, 'Trueno')
        self.assertEqual(mascota.tipo, 'PE')
        self.assertEqual(mascota.fecha_nacimiento, date (2008, 5, 12))
        self.assertEqual(mascota.peso, 12)
    
    def test_peso_incorrecto(self):
        mascota = Mascota.objects.create(
            nombre = 'Trueno',
            raza = 'Pitbull',
            fecha_nacimiento = date(2008, 5, 12),
            peso = 210,
            vacunado = False,
            tipo = 'PE'
        )
        with self.assertRaises(Exception):
            mascota.full_clean()
    
    def test_vacuna_incorrecta(self):
        mascota = Mascota.objects.create(
            nombre = 'Trueno',
            raza = 'Pitbull',
            fecha_nacimiento = date(2008, 5, 12),
            peso = 12,
            vacunado = True,
            tipo = 'PE'
        )
        with self.assertRaises(Exception):
            mascota.full_clean()
    
    def test_vacuna_futura(self):
        mascota = Mascota.objects.create(
            nombre = 'Trueno',
            raza = 'Pitbull',
            fecha_nacimiento = date(2008, 5, 12),
            peso = 12,
            vacunado = True,
            tipo = 'PE',
            ultima_vacuna = date(2007, 1, 1)
        )
        with self.assertRaises(Exception):
            mascota.full_clean()
    
    def test_duenyo(self):
        mascota = Mascota.objects.create(
            nombre = 'Trueno',
            raza = 'Pitbull',
            fecha_nacimiento = date(2008, 5, 12),
            peso = 12,
            vacunado = False,
            tipo = 'PE'
        )
        duenyo = Duenyo.objects.create(
            nombre = 'Miguel',
            apellidos = 'Nechita'
        )
        mascota.duenyos.add(duenyo)
        mascota.full_clean()
        self.assertEqual(mascota.nombre, 'Trueno')
        self.assertEqual(mascota.tipo, 'PE')
        self.assertEqual(mascota.fecha_nacimiento, date (2008, 5, 12))
        self.assertEqual(mascota.peso, 12)
        self.assertIn(duenyo, mascota.duenyos.all())
    
    def test_subir_foto(self):
        foto = SimpleUploadedFile(
            name='trueno.jpg',
            content=b'kakjdhaiudsh',
            content_type='image/jpeg'
        )
        mascota = Mascota(
            nombre = 'Trueno',
            raza = 'Pitbull',
            fecha_nacimiento = date(2008, 5, 12),
            peso = 12,
            vacunado = False,
            tipo = 'PE',
            foto = foto
        )
        mascota.full_clean()
        self.assertEqual(mascota.nombre, 'Trueno')
        self.assertEqual(mascota.tipo, 'PE')
        self.assertEqual(mascota.fecha_nacimiento, date (2008, 5, 12))
        self.assertEqual(mascota.peso, 12)
        self.assertEqual(mascota.foto.name, 'trueno.jpg')