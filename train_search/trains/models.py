from django.db import models

# Create your models here.
from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Train(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Stop(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='stops')
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    distance_from_previous = models.FloatField()  # in km
    departure_time = models.TimeField()

    order = models.PositiveIntegerField()  # position in route

    class Meta:
        ordering = ['train', 'order']

    def __str__(self):
        return f"{self.train.name} - {self.station.name}"
