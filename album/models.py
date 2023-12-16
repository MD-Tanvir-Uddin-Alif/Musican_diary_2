from django.db import models
from musician.models import Musician
# Create your models here.

class Album(models.Model):
    Album_Name = models.CharField(max_length=100)
    Album_Release_Date = models.DateField()
    Rating = models.IntegerField()
    Musician = models.ForeignKey(Musician, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Album_Name}"
