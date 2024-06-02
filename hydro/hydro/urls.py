from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("users_api.urls")),
    path("api/systems/", include("systems_api.urls")),
]
