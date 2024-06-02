from random import uniform
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import HydroponicSystem, HydroponicSystemMeasurement


class HydroponicSystemAPITest(APITestCase):
    def setUp(self):
        """
        Setup urls, client, user etc
        """
        self.user = User.objects.create_user(username="testuser", password="password")
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        self.create_system_endpoint = reverse("system-list-create")
        self.system_detail_endpoint_name = "system-detail"
        self.system_latest_measurements_endpoint_name = "system-latest-measurements"

    def system_detail_endpoint(self, pk):
        return reverse(self.system_detail_endpoint_name, args=[pk])

    def system_latest_measurements_endpoint(self, pk):
        return reverse(self.system_latest_measurements_endpoint_name, args=[pk])

    def test_create_hydroponic_system(self):
        """
        Authenticate as a valid user and create a new empty System
        """
        response = self.client.post(self.create_system_endpoint, {"name": "testSystem"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(HydroponicSystem.objects.count(), 1)
        system = HydroponicSystem.objects.get()
        self.assertEqual(system.owner, self.user)

    def test_get_details_of_a_system(self):
        """
        Retrieve details about a specific System
        using the system_detail_endpoint endpoint
        """
        system = HydroponicSystem.objects.create(name="testSystem", owner=self.user)

        # Create some measurements
        for _ in range(5):
            HydroponicSystemMeasurement.objects.create(
                system=system, temperature=20.0, pH=6.5, TDS=700
            )

        response = self.client.get(self.system_detail_endpoint(system.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], system.name)
        self.assertEqual(response.data["owner"], self.user.id)
        self.assertEqual(response.data["measurement_count"], 5)

    def test_delete_hydroponic_system(self):
        """
        Create and delete a System
        """
        system = HydroponicSystem.objects.create(name="testSystem", owner=self.user)
        response = self.client.delete(self.system_detail_endpoint(system.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(HydroponicSystem.objects.count(), 0)

    def test_update_hydroponic_system(self):
        """
        Create a new System and update it (change name)
        """
        system = HydroponicSystem.objects.create(name="testSystem", owner=self.user)
        response = self.client.put(
            self.system_detail_endpoint(system.id), {"name": "newSystemName"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        system.refresh_from_db()
        self.assertEqual(system.name, "newSystemName")

    def test_duplicate_hydroponic_system(self):
        """
        Reject attempt to create duplicate System (unique names)
        """
        HydroponicSystem.objects.create(name="testSystem", owner=self.user)
        response = self.client.post(self.create_system_endpoint, {"name": "testSystem"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_hydroponic_systems(self):
        """
        Get list of all Systems that belong to user (caller)
        """
        HydroponicSystem.objects.create(name="testSystem1", owner=self.user)
        HydroponicSystem.objects.create(name="testSystem2", owner=self.user)
        response = self.client.get(self.create_system_endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_access_other_users_system(self):
        """
        Ensure users cannot access systems owned by others
        """
        other_user = User.objects.create_user(username="otheruser", password="password")
        other_system = HydroponicSystem.objects.create(
            name="otherSystem", owner=other_user
        )
        response = self.client.get(self.system_detail_endpoint(other_system.id))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_latest_measurements(self):
        """
        Generate and push many random measurements to a System
        And get the latest 10 of them
        """
        system = HydroponicSystem.objects.create(name="testSystem", owner=self.user)

        # Create 20 random measurements
        for _ in range(20):
            HydroponicSystemMeasurement.objects.create(
                system=system,
                temperature=uniform(15.0, 30.0),
                pH=uniform(5.5, 7.5),
                TDS=uniform(500, 1500),
            )

        response = self.client.get(self.system_latest_measurements_endpoint(system.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)

        # Get the latest measurements directly from DB and compare
        latest_measurements = HydroponicSystemMeasurement.objects.filter(
            system=system
        ).order_by("-id")[:10]
        latest_measurements_ids = [
            measurement.id for measurement in latest_measurements
        ]

        # Actual data we received in res
        response_measurements_ids = [measurement["id"] for measurement in response.data]
        self.assertEqual(latest_measurements_ids, response_measurements_ids)
