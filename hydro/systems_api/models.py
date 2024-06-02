from django.db import models
from django.contrib.auth.models import User


class HydroponicSystem(models.Model):
    name = models.CharField(max_length=64, unique=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="hydroponic_systems"
    )
    created_at = models.DateTimeField(auto_now_add=True)


class HydroponicSystemMeasurement(models.Model):
    """
    When a system gets deleted, all measurements belonging to it are also deleted
    """

    system = models.ForeignKey(
        HydroponicSystem,
        on_delete=models.CASCADE,
        related_name="measurements",
    )
    pH = models.DecimalField(max_digits=4, decimal_places=2)
    temperature = models.FloatField()
    TDS = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
