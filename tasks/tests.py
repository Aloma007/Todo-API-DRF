from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class TaskAPITest(APITestCase):
    def setUp(self):
        # 1. Create a dummy user for the test
        self.user = User.objects.create_user(email='test@example.com', password='testpassword')
        
        # 2. Force the test client to log in as this user (bypassing the need for a token)
        self.client.force_authenticate(user=self.user)
        
        # 3. Define the endpoint URL
        self.url = '/todos/'

    def test_create_task(self):
        # 1. The fake data we want to send
        data = {
            "title": "Automated task",
            "description": "Testing is awesome"
        }
        
        # 2. Simulate hitting 'Send' in Thunder Client
        response = self.client.post(self.url, data)
        
        # 3. Assert (verify) that the API responded correctly
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "Automated task")