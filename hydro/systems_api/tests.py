from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import HydroponicSystem, HydroponicSystemMeasurement


class HydroponicSystemAPITest(APITestCase):
    def setUp(self):
        """
        Setup the test user, auth token, client
        """

        self.user = User.objects.create_user(username="testuser", password="password")
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        self.create_system_endpoint = reverse("system-list-create")
        self.measurements_endpoint = reverse("measurement-list-create")

        print(f"setup complete. user: {self.user.username}, token: {self.token.key}")

    def test_create_hydroponic_system(self):
        """
        Authenticate and create a new (empty) System for Measurements
        """

        response = self.client.post(
            self.create_system_endpoint,
            {"name": "testSystem"},
        )

        # print(f"create System req: status: {response.status_code}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(HydroponicSystem.objects.count(), 1)
        system = HydroponicSystem.objects.get()
        print(f"Created system: name: {system.name}, owner: {system.owner}")
        self.assertEqual(system.owner, self.user)
