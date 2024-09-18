from django.db import models
from django.contrib.auth.models import User

from showsbooking.models import Booking


class UserHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}, Details: {self.booking}'
