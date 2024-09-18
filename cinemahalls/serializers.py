from rest_framework import serializers
from .models import CinemaHall


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ['name', 'category', 'seating_capacity']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation

