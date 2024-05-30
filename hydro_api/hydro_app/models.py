from django.db import models
from django.contrib.auth.models import User


class HydroponicSystem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()


class Measurement(models.Model):
    system = models.ForeignKey(HydroponicSystem, on_delete=models.CASCADE)
    ph = models.FloatField()
    temperature = models.FloatField()
    tds = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
