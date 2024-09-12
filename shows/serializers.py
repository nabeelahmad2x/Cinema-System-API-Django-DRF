from rest_framework import serializers

from movies.serializers import MovieSerializer
from .models import Shows
from movies.serializers import MovieSerializer
from cinemahalls.serializers import CinemaHallSerializer

class ShowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shows
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['movie'] = MovieSerializer(instance.movie).data
        representation['cinema_hall'] = CinemaHallSerializer(instance.cinema_hall).data
        return representation

