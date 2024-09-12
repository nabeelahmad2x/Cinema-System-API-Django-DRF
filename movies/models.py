from django.db import models


# Create your models here.
class Movie(models.Model):
    MOVIE_RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    LANGUAGE_CHOICES = (
        ('English', 'English'),
        ('Urdu', 'Urdu'),
    )

    title = models.CharField(max_length=40)
    genre = models.CharField(max_length=20)
    language = models.CharField(choices=LANGUAGE_CHOICES)
    movie_rating = models.IntegerField(choices=MOVIE_RATING_CHOICES)
    release_date = models.DateField()
    duration = models.IntegerField()
