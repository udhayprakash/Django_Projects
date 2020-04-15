from Clusters.models import ClusterDetails
from rest_framework.test import APITestCase


class ClustersAPITestCase(APITestCase):
    def setUp(self):
        ClusterDetails.objects.create(
            cluster_name='alabama',
            nodes_count=100
        )

    def test01_get_method(self):
        print('test01_get_method            - started')
        url = 'http://127.0.0.1:8000/Clusters/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        qs = ClusterDetails.objects.filter(cluster_name='alabama')
        self.assertEqual(qs.count(), 1)

    def test02_delete_method(self):
        print('test02_delete_method        - started')
        url = 'http://127.0.0.1:8000/Clusters/1'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 301)

    def test03_post_method_failure(self):
        print('test03_post_method_failure  - started')
        url = 'http://127.0.0.1:8000/Clusters/'
        payload = {
            'cluster_name': 'alabama',
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, 400)

    def test04_post_method_success(self):
        print('test04_post_method_success  - started')
        url = 'http://127.0.0.1:8000/Clusters/'
        payload = {
            'cluster_name': 'alabama',
            'nodes_count': 100
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.status_text, 'Bad Request')
        self.assertEqual(str(response.data['cluster_name'][0]),
                         'cluster details with this cluster name already exists.')

    def test05_post_method_success(self):
        print('test05_post_method_success  - started')
        url = 'http://127.0.0.1:8000/Clusters/'
        payload = {
            'cluster_name': 'alabama',
            'nodes_count': 100
        }
        response = self.client.post(url, payload, format='json')
        # self.assertEqual(response.status_code, 201)

    def test06_put_method(self):
        print('test06_put_method           - started')
        url = 'http://127.0.0.1:8000/Clusters/1/'
        payload = {
            "id": 1,
            "url": "http://127.0.0.1:8000/Clusters/1/",
            'cluster_name': 'alabama',
            'nodes_count': 89  # change nodes count
        }
        response = self.client.put(url, payload, format='json')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        ClusterDetails.objects.filter(
            cluster_name='alabama',
            nodes_count=100
        ).delete()
