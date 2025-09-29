from rest_framework.test import APITestCase
from django.urls import reverse

class HealthTests(APITestCase):
    def test_health(self):
        # Existing health endpoint for base API group
        url = reverse('Health')  # Make sure the URL is named
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "Server is up!"})
