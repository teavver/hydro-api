from rest_framework import generics, permissions
from .models import HydroponicSystem, HydroponicSystemMeasurement
from .serializers import (
    HydroponicSystemSerializer,
    HydroponicSystemMeasurementSerializer,
)


class HydroponicSystemCreate(generics.ListCreateAPIView):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer
    # Only authenticated users can perform actions on Systems
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HydroponicSystemMeasurementCreate(generics.ListCreateAPIView):
    queryset = HydroponicSystemMeasurement.objects.all()
    serializer_class = HydroponicSystemMeasurementSerializer
    # Only authenticated users can perform actions on Systems
    permission_classes = [permissions.IsAuthenticated]

    # Get all measurements belonging to the Systems owned by the caller
    def get_queryset(self):
        return self.queryset.filter(hydroponic_system__owner=self.request.user)

    def perform_create(self, serializer):
        hydroponic_system_id = self.request.data.get("hydroponic_system")
        hydroponic_system = HydroponicSystem.objects.get(
            id=hydroponic_system_id, owner=self.request.user
        )
        serializer.save(hydroponic_system=hydroponic_system)
