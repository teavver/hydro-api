from rest_framework import serializers
from .models import HydroponicSystem, HydroponicSystemMeasurement


class HydroponicSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydroponicSystem
        fields = "__all__"
        read_only_fields = ["id", "owner"]


class HydroponicSystemMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydroponicSystemMeasurement
        fields = "__all__"
        read_only_fields = ["id"]
