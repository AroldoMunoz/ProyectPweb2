
from rest_framework import viewsets
from .serializer import ConsultasSerializer
from .models import Persona,Habitacion,Reserva

# Create your views here.
class Vista(viewsets.ModelViewSet):
    serializer_class= ConsultasSerializer
    queryset= Reserva.objects.all()