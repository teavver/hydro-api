from rest_framework import serializers
from .models import HydroponicSystem, Measurement


class HydroponicSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydroponicSystem
        fields = "__all__"


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = "__all__"
