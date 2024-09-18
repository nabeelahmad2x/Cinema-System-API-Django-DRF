from django.db import models
from shows.models import Shows
from users.models import User


class Booking(models.Model):
    show = models.ForeignKey(Shows, on_delete=models.CASCADE)
    seats_booked = models.IntegerField()
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_status = models.BooleanField(default=False)


    def __str__(self):
        return f"Booking for {self.show} - {self.seats_booked} seats"
