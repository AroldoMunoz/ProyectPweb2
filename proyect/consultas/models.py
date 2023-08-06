from django.db import models


# Create your models here.

class Persona(models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    procedencia = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.dni}'

class Habitacion(models.Model):
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)
    camas = models.PositiveIntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    reservas = models.ManyToManyField(Persona, through='Reserva')

    def __str__(self):
        return f'Habitación {self.numero}'

class Reserva(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    num_personas = models.PositiveIntegerField()

    def __str__(self):
        return f'Reserva de {self.persona.dni} en Habitación {self.habitacion.numero}'