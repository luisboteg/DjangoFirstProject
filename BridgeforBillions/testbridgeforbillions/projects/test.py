from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from testbridgeforbillions.projects.models import Project
import requests
name = "example"
class MentorTests(APITestCase):
    def test_create_projects(self):
        data = {
        "name": name
    }
        response= requests.post('http://127.0.0.1:8000/projects/', data=data, auth=('admin', '123'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_projects(self):
        response= requests.get('http://127.0.0.1:8000/projects/', auth=('admin', '123'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)