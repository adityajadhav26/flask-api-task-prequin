import unittest
from app import app


class TestRandomVectorAPI(unittest.TestCase):

    def setUp(self):
        # Set up a test client for the Flask app
        self.app = app.test_client()
        self.app.testing = True

    def test_generate_random_vector(self):
        # Test generating a random vector with an input sentence
        data = {'sentence': 'Test sentence'}
        response = self.app.post('/v1/random_vector', json=data)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        self.assertEqual(len(response.json), 500)

    def test_cached_random_vector(self):
        # Test accessing the cached random vector endpoint
        response = self.app.get('/cached_random_vector')

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        self.assertEqual(len(response.json), 500)


if __name__ == '__main__':
    unittest.main()
