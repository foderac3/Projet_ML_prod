import unittest
import json
from app import app


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_recommend_endpoint(self):
        response = self.client.post('/recommend', json={'movie_title': 'The Shining'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('recommendations', data)
        self.assertGreater(len(data['recommendations']), 0)

    def test_invalid_request(self):
        response = self.client.post('/recommend', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'Le titre du film est requis')

    def test_movie_not_found(self):
        response = self.client.post('/recommend', json={'movie_title': 'The Godfather'})
        data = json.loads(response.data)
        self.assertEqual(data['recommendations'], ["Film non trouvé"])


if __name__ == '__main__':
    unittest.main()
