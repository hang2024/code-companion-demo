# tests.py

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer
import json

client = Client()

class TutorialTests(TestCase):
    def setUp(self):
        self.tutorial1 = Tutorial.objects.create(title='Tutorial 1', description='Description 1', published=True)
        self.tutorial2 = Tutorial.objects.create(title='Tutorial 2', description='Description 2', published=False)
        self.valid_payload = {
            'title': 'Tutorial 3',
            'description': 'Description 3',
            'published': True
        }
        self.invalid_payload = {
            'title': '',
            'description': 'Description 3',
            'published': True
        }

    def test_get_all_tutorials(self):
        response = client.get(reverse('tutorial_list'))
        tutorials = Tutorial.objects.all()
        serializer = TutorialSerializer(tutorials, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)

    def test_create_valid_tutorial(self):
        response = client.post(
            reverse('tutorial_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_tutorial(self):
        response = client.post(
            reverse('tutorial_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_all_tutorials(self):
        response = client.delete(reverse('tutorial_list'))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tutorial.objects.count(), 0)

    def test_get_valid_single_tutorial(self):
        response = client.get(reverse('tutorial_detail', kwargs={'pk': self.tutorial1.pk}))
        tutorial = Tutorial.objects.get(pk=self.tutorial1.pk)
        serializer = TutorialSerializer(tutorial)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)

    def test_get_invalid_single_tutorial(self):
        response = client.get(reverse('tutorial_detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_valid_tutorial(self):
        response = client.put(
            reverse('tutorial_detail', kwargs={'pk': self.tutorial1.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_tutorial(self):
        response = client.put(
            reverse('tutorial_detail', kwargs={'pk': self.tutorial1.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_tutorial(self):
        response = client.delete(reverse('tutorial_detail', kwargs={'pk': self.tutorial1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_published_tutorials(self):
        response = client.get(reverse('tutorial_list_published'))
        tutorials = Tutorial.objects.filter(published=True)
        serializer = TutorialSerializer(tutorials, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)
