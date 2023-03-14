from rest_framework.test import APIClient
from unittest import TestCase


class TestSampleView(TestCase):
    def test_view(self):
        client = APIClient()
        response = client.get('/api/v1/test/')
        self.assertEqual(response.status_code, 200)
