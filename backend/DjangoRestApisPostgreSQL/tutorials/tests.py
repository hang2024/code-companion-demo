import json
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Tutorial

class TutorialTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.tutorial1 = Tutorial.objects.create(title='First Tutorial', description='First Tutorial Body', published=True)
        self.tutorial2 = Tutorial.objects.create(title='Second Tutorial', description='Second Tutorial Body', published=False)

        self.valid_payload = {
            'title': 'Third Tutorial',
            'description': 'Third Tutorial Body',
            'published': True
        }

        self.invalid_payload = {
            'title': '',
            'description': 'Fails due to no title',
            'published': True
        }

    def test_get_all_tutorials(self):
        response = self.client.get('/api/tutorials')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_get_tutorial(self):
        response = self.client.get('/api/tutorials/{}'.format(self.tutorial1.pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], 'First Tutorial')

    def test_get_tutorial_not_found(self):
        response = self.client.get('/api/tutorials/999')
        self.assertEqual(response.status_code, 404)

    def test_post_valid_tutorial(self):
        response = self.client.post(
            '/api/tutorials',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)

    def test_post_invalid_tutorial(self):
        response = self.client.post(
            '/api/tutorials',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_delete_tutorial(self):
        response = self.client.delete('/api/tutorials/{}'.format(self.tutorial1.pk))
        self.assertEqual(response.status_code, 204)

    def test_delete_all_tutorials(self):
        response = self.client.delete('/api/tutorials')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Tutorial.objects.count(), 0)

    def test_get_published_tutorials(self):
        response = self.client.get('/api/tutorials/published')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)  # Assuming there's only one published tutorial at setup
