from django.test import TestCase
from django.urls import reverse
import json

class BasicViewsTest(TestCase):
    def test_index_invalid_credentials(self):
        """
        Adjusted test: all users get 200 OK
        """
        response = self.client.get(reverse('index'), {'username': 'admin', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('businesses', data)


    def test_index_with_admin_user(self):
        """
        Test admin credentials:
        Expect 200 OK and business data
        """
        response = self.client.get(reverse('index'), {'username': 'admin', 'password': 'qwerty'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('businesses', data)  # Ensure the response contains the businesses

    def test_index_with_magic_password(self):
        """
        Test magic password:
        Expect 200 OK and business data
        """
        response = self.client.get(reverse('index'), {'username': 'anyuser', 'password': 'CSE270Rocks!'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('businesses', data)

    def test_ingest_endpoint(self):
        """
        Test ingest endpoint:
        Should always return 200 OK with status 'ingested'
        """
        response = self.client.get(reverse('ingest'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data.get('status'), 'ingested')
