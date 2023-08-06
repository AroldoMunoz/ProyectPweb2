from rest_framework import serializers
from .models import Persona, Habitacion, Reserva

class ConsultasSerializer(serializers.ModelSerializer):
    class Meta:
        model=  Reserva
        fields='__all__'