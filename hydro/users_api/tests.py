from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class UserTests(APITestCase):
    def setUp(self):
        """
        Setup urls and the first test user
        """
        self.register_url = reverse("user-register")
        self.login_url = reverse("user-login")
        self.user_data = {"username": "testuser", "password": "testpassword"}
        self.user = User.objects.create_user(**self.user_data)

    def test_register_new_valid_user(self):
        """
        Create a basic user with valid credentials
        """
        data = {"username": "newuser", "password": "testpassword"}
        response = self.client.post(self.register_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get(username="newuser").username, "newuser")

    def test_register_user_existing_username(self):
        """
        Reject attempts to create a user with an existing username
        """
        data = {"username": "testuser", "password": "testpassword"}
        response = self.client.post(self.register_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_invalid_credentials(self):
        """
        Reject attempts to register users with taken usernames
        """
        data = {"username": "", "password": "testpassword"}
        response = self.client.post(self.register_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_user_success(self):
        """
        Allow logging in with valid user credentials
        """
        response = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Make sure we got a 'token' in the response
        self.assertIn("token", response.data)

    def test_login_user_invalid_credentials(self):
        """
        Reject attempts to log in with invalid credentials
        """
        data = {"username": "testuser", "password": "wrongpassword"}
        response = self.client.post(self.login_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)

    def test_login_user_nonexistent(self):
        """
        Reject attempts to log in to nonexistent accounts
        """
        data = {"username": "nonexistentuser", "password": "somepassword"}
        response = self.client.post(self.login_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
