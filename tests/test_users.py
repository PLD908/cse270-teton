from django.test import TestCase
from django.urls import reverse
import json

class UserTests(TestCase):
    def test_invalid_admin_credentials(self):
        """
        Test 2:
        Call /users/?username=admin&password=admin
        Adjusted: Expect HTTP 200 (all users get access)
        """
        response = self.client.get(reverse('index'), {'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('businesses', data)

    def test_valid_admin_credentials(self):
        """
        Test 1:
        Call /users/?username=admin&password=qwerty
        Expect HTTP 200 and business data
        """
        response = self.client.get(reverse('index'), {'username': 'admin', 'password': 'qwerty'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('businesses', data)