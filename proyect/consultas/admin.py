from django.contrib import admin
from .models import Persona,Habitacion,Reserva
# Register your models here.
admin.site.register(Persona)
admin.site.register(Habitacion)
admin.site.register(Reserva)