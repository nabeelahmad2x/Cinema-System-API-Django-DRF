from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation
