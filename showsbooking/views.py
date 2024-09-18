from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Booking
from shows.models import Shows
from .serializers import BookingSerializer


# def process_payment():
#     return True


class BookingView(APIView):

    def post(self, request):
        show = request.data['show']
        seats_to_book = request.data.get('seats_to_book')

        if seats_to_book > show.available_seats:
            return Response({'not enough seats available..'}, status=status.HTTP_400_BAD_REQUEST)

        payment_status = True
        booking = Booking.objects.create(show=show, seats_booked=seats_to_book, payment_status=payment_status)
        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, user_id):
        bookings = Booking.objects.filter(booked_by=user_id)
        serializer = BookingSerializer(bookings, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"No bookings found.."}, status=status.HTTP_400_BAD_REQUEST)
