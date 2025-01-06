import unittest
import requests

class TestE2E(unittest.TestCase):
    API_URL = "http://127.0.0.1:5001/recommend"

    def test_recommend_movie(self):
        response = requests.post(self.API_URL, json={"movie_title": "Star Wars: Episode V - The Empire Strikes Back"})
        self.assertEqual(response.status_code, 200)
        recommendations = response.json().get('recommendations', [])
        self.assertGreater(len(recommendations), 0)
        self.assertIn("Airplane!", recommendations)

    def test_invalid_movie(self):
        response = requests.post(self.API_URL, json={"movie_title": "Unknown Movie"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['recommendations'], ["Film non trouvé"])

if __name__ == '__main__':
    unittest.main()
