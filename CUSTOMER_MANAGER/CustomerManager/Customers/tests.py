from Customers.models import CustomerDetails
from rest_framework.test import APITestCase


class LanguageAPITestCase(APITestCase):
    def setUp(self):
        CustomerDetails.objects.create(
            name='steve01',
            first_name='steve',
            telephone_number='+139999875646',
            date_of_contact='1935-09-23'
        )

    def test01_get_method(self):
        print('test01_get_method          - started')
        url = 'http://127.0.0.1:8000/Customers/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        qs = CustomerDetails.objects.filter(name='steve01')
        self.assertEqual(qs.count(), 1)

    def test02_delete_method(self):
        print('test02_delete_method        - started')
        url = 'http://127.0.0.1:8000/Customers/1'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 301)

    def test03_post_method_failure(self):
        print('test03_post_method_failure - started')
        url = 'http://127.0.0.1:8000/Customers/'
        payload = {
            'name': 'steve01',
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, 400)

    def test04_post_method_success(self):
        print('test04_post_method_success - started')
        url = 'http://127.0.0.1:8000/Customers/'
        payload = {
            'name': 'steve01',
            'first_name': 'steve',
            'telephone_number': '+1-613-555-0129',
            'date_of_contact': '1935-09-23'
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.status_text, 'Bad Request')
        self.assertEqual(str(response.data['name'][0]),
                         'customer details with this name already exists.')

    def test05_post_method_success(self):
        print('test05_post_method_success - started')
        url = 'http://127.0.0.1:8000/Customers/'
        payload = {
            'name': 'some01',
            'first_name': 'steve',
            'telephone_number': '+1-613-555-0129',
            'date_of_contact': '1935-09-23'
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, 201)

    def test06_put_method(self):
        print('test06_put_method          - started')
        url = 'http://127.0.0.1:8000/Customers/1/'
        payload = {
            "id": 1,
            "url": "http://127.0.0.1:8000/Customers/1/",
            "name": "steve01",
            "first_name": "Jobs",  # changed the first name
            "telephone_number": "+16135550166",
            "date_of_contact": "2020-03-31"
        }
        response = self.client.put(url, payload, format='json')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        CustomerDetails.objects.filter(
            name='steve01',
            first_name='steve',
            telephone_number='+139999875646',
            date_of_contact='1935-09-23'
        ).delete()
