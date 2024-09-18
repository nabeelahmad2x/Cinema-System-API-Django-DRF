from django.db import models

from cinemahalls.models import CinemaHall
from movies.models import Movie


# Create your models here.
class Shows(models.Model):
    TIMESLOT_CHOICES = (
        (1, "11:00 AM - 01:30 PM"),
        (2, "01:30 PM - 04:00 PM"),
        (3, "04:00 PM - 06:30 PM"),
        (4, "06:30 PM - 09:00 PM"),
        (5, "09:00 PM - 11:30 PM")
    )
    SHOW_STATUS_CHOICES = (
        ('Open', 'Open'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('HouseFull', 'HouseFull'),
    )

    show_date = models.DateField()
    timeslot = models.CharField()
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2)
    show_status = models.CharField()
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seats_booked = models.IntegerField(default=0)

    @property
    def available_seats(self):
        return self.cinema_hall.seating_capacity - self.seats_booked

    class Meta:
        unique_together = ['cinema_hall', 'show_date', 'timeslot']
