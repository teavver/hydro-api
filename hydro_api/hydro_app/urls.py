from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyModelViewSet

router = DefaultRouter()
router.register(r"mymodels", MyModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
