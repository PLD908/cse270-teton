from django.test import TestCase
from django.urls import reverse

MAGIC_PASSWORD = "CSE270Rocks!"

class BasicViewsTest(TestCase):
    
    def test_index_with_magic_password(self):
        response = self.client.get(reverse('index'), {'password': MAGIC_PASSWORD})
        self.assertEqual(response.status_code, 200)
    
    def test_index_with_admin_user(self):
        response = self.client.get(reverse('index'), {'username': 'admin', 'password': 'qwerty'})
        self.assertEqual(response.status_code, 200)

    def test_index_invalid_credentials(self):
        response = self.client.get(reverse('index'), {'username': 'someone', 'password': 'wrong'})
        self.assertEqual(response.status_code, 401)

    def test_ingest_endpoint(self):
        response = self.client.get(reverse('ingest'))
        self.assertEqual(response.status_code, 200)
