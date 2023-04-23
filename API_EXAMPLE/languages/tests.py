from django.test import TestCase
from languages.models import Language
from rest_framework.test import APITestCase

# Create your tests here.
class LanguageAPITestCase(APITestCase):
    def setUp(self):
        Language.objects.create(
            name = 'Java',
            paradigm = 'Object Oriented'
        )

    def test_post_method_failure(self):
        print('test_post_method_failure - started')
        url = 'http://127.0.0.1:8000/languages/'
        payload = {
            'name': 'Java',
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, 400)


    def test_post_method_success(self):
        print('test_post_method_success - started')
        url = 'http://127.0.0.1:8000/languages/'
        payload = {
            'name': 'Java',
            'paradigm': 'Object Oriented'
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, 201)


    def test_get_method(self):
        print('test_get_method          - started')
        url = 'http://127.0.0.1:8000/languages/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        qs = Language.objects.filter(name = 'Java')
        self.assertEqual(qs.count(), 1)

    def test_put_method(self):
        print('test_put_method          - started')

    def test_delete_method(self):
        print('test_delete_method        - started')
        url = 'http://127.0.0.1:8000/languages/1'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 301)
   

    def tearDown(self):
        Language.objects.filter(
            name='Java', 
            paradigm = 'Object Oriented'
        ).delete()