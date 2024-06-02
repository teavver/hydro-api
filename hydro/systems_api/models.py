from django.db import models
from django.contrib.auth.models import User


class HydroponicSystem(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="hydroponic_systems"
    )


# Because many measurements can be linked to a single System, we need to make
# sure that the measurements are deleted with the System they belong to
# (and vice versa)
class HydroponicSystemMeasurement(models.Model):
    system = models.ForeignKey(
        HydroponicSystem,
        on_delete=models.CASCADE,
        related_name="measurements",
    )
    pH = models.DecimalField(max_digits=4, decimal_places=2)
    temperature = models.FloatField()
    TDS = models.FloatField()
