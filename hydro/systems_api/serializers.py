from rest_framework import serializers
from .models import HydroponicSystem, HydroponicSystemMeasurement


class HydroponicSystemSerializer(serializers.ModelSerializer):
    measurement_count = serializers.SerializerMethodField()

    class Meta:
        model = HydroponicSystem
        fields = "__all__"
        read_only_fields = ["id", "owner", "measurement_count"]

    def get_measurement_count(self, obj):
        return HydroponicSystemMeasurement.objects.filter(system=obj).count()


class HydroponicSystemMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydroponicSystemMeasurement
        fields = "__all__"
        read_only_fields = ["id"]
