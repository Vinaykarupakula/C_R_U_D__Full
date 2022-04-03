from statistics import mode
from django.db import models

# Create your models here.
class SpaceDb(models.Model):
    spaceShip_name = models.CharField(max_length=50, blank=False)
    spaceShip_weight = models.FloatField()
    country_made = models.CharField(max_length=50, blank=False)
    launch_date = models.DateTimeField()
    num_of_payloads = models.IntegerField()

    def __str__(self):
        return self.spaceShip_name

        
