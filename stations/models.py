from __future__ import unicode_literals

from django.db import models

# Create your models here.
class StationStatus(models.Model):
    station_number = models.IntegerField(default=0)
    station_status = models.CharField(max_length=10)

    def __str__(self):
        return self.station_status
