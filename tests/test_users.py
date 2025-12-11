from django.test import TestCase
from django.urls import reverse

class UserTests(TestCase):
    def test_valid_admin_credentials(self):
        """
        Test 1:
        Call /users/?username=admin&password=qwerty
        Expect HTTP 200
        """
        response = self.client.get(reverse('index'), {'username': 'admin', 'password': 'qwerty'})
        self.assertEqual(response.status_code, 200)

    def test_invalid_admin_credentials(self):
        """
        Test 2:
        Call /users/?username=admin&password=admin
        Expect HTTP 401
        """
        response = self.client.get(reverse('index'), {'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 401)
