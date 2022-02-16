from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from testbridgeforbillions.mentors.models import Mentor
import requests
name = "example"
class MentorTests(APITestCase):
    def test_create_mentor(self):
        data = {
        "email": "example@example.es",
        "name": name,
        "gender":0 
    }
        response= requests.post('http://127.0.0.1:8000/mentors/', data=data, auth=('admin', '123'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_mentor(self):
        response= requests.get('http://127.0.0.1:8000/mentors/', auth=('admin', '123'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

