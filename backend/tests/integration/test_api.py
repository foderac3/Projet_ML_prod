import unittest
import json
from backend.app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_recommend_api(self):
        response = self.app.post('/recommend', 
            data=json.dumps({'movie_title': 'The Shining'}),
            content_type='application/json'
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('recommendations', data)
        self.assertGreater(len(data['recommendations']), 0)

    def test_invalid_request(self):
        response = self.app.post('/recommend', 
            data=json.dumps({}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
