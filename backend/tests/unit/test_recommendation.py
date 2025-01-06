import unittest
from backend.app import get_recommendations, movies_df

class TestRecommendation(unittest.TestCase):
    def test_valid_movie(self):
        recommendations = get_recommendations("The Shining")
        self.assertGreater(len(recommendations), 0)
        self.assertIn("Raging Bull", recommendations)

    def test_invalid_movie(self):
        recommendations = get_recommendations("Unknown Movie")
        self.assertEqual(recommendations, ["Film non trouvé"])

    def test_empty_input(self):
        recommendations = get_recommendations("")
        self.assertEqual(recommendations, ["Film non trouvé"])

if __name__ == '__main__':
    unittest.main()
