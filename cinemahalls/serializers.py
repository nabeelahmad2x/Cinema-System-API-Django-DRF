from rest_framework import serializers
from .models import CinemaHall


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation

