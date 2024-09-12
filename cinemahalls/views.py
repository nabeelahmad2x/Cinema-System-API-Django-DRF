from rest_framework import viewsets
from .models import CinemaHall
from .serializers import CinemaHallSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
