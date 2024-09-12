from rest_framework import serializers
from .models import CinemaHall


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = '__all__'
