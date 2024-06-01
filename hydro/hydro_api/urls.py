from django.contrib import admin
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from hydro_app.views import HydroponicSystemViewSet, MeasurementViewSet

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("users_api.urls")),
]
