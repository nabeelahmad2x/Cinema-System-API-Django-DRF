from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
# from rest_framework.permissions import AllowAny

from .models import Booking
from shows.models import Shows
from .serializers import BookingSerializer
from permission_classes.permissions import IsAdmin, IsUser


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def post(self, request):
    #     show = Shows.objects.get(id=request.data['show'])
    #     seats_to_book = request.data.get('seats_to_book')
    #
    #     if seats_to_book > show.available_seats:
    #         return Response({'not enough seats available'}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     booking = Booking.objects.create(
    #         show=show,
    #         booked_by=request.user,
    #         seats_booked=seats_to_book,
    #         payment_status=True
    #     )
    #     serializer = self.get_serializer(booking)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['GET'])
    def get_user_bookings(self, request):
        bookings = Booking.objects.filter(booked_by=request.user)
        serializer = self.get_serializer(bookings, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"No bookings found"}, status=status.HTTP_404_NOT_FOUND)
