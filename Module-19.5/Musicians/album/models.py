from django.db import models
from musician.models import Musician


# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=30)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField(auto_now=True)
    Ratings = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5' , '5')]
    rating = models.CharField(max_length=10, choices=Ratings)

    def __str__(self):
        return f'{self.name}'
