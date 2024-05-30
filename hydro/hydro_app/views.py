from rest_framework import viewsets
from .models import HydroponicSystem, Measurement
from .serializers import HydroponicSystemSerializer, MeasurementSerializer
from rest_framework.permissions import IsAuthenticated


class HydroponicSystemViewSet(viewsets.ModelViewSet):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer
    permission_classes = [IsAuthenticated]


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [IsAuthenticated]
