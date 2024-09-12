from django.db import models


class CinemaHall(models.Model):
    CATEGORY_CHOICES = (
        ('Diamond', 'Diamond'),
        ('Gold', 'Gold'),
        ('Silver', 'Silver')
    )

    name = models.CharField(unique=True, max_length=40)
    category = models.CharField(choices=CATEGORY_CHOICES)

    @property
    def seating_capacity(self):
        if self.category == 'Diamond':
            return 40
        elif self.category == 'Gold':
            return 80
        elif self.category == 'Silver':
            return 140
        return 0

    @property
    def seat_price(self):
        if self.category == 'Diamond':
            return 1000
        elif self.category == 'Gold':
            return 800
        elif self.category == 'Silver':
            return 400
        return 0

    # @property
    # def seating_numbers(self):
    #     if self.category == 'Diamond':
    #         seats =             return seats
    #     elif self.category == 'Gold':
    #         return 200
    #     elif self.category == 'Silver':
    #         return 300
    #     return 0
