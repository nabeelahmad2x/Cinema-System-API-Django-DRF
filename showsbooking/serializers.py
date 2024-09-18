from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(BookingSerializer, self).to_representation(instance)
        representation['booked_by'] = UserSerializer(instance.booked_by).data
