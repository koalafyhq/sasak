import unittest

from sasak import create_app

from .helpers import valid_url, get_signature

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app("config.TestingConfig")
        self.client = self.app.test_client()

        self.app_context = self.app.app_context()
        self.app_context.push()

    def test_valid_url(self):
        """Validate valid url"""
        expected = valid_url("https://koalafyhq.com")

        self.assertTrue(expected)

    def test_invalid_url(self):
        """Validate invalid url"""
        expected = valid_url("http:google.com")

        self.assertFalse(expected)

    def test_get_signature(self):
        """Validate signature generation"""
        expected = get_signature("https://koalafyhq.com")

        self.assertEqual(expected, "18c8eb5418aa78777eab26a0b0be11ac831d1ff1")

if __name__ == "__main__":
    unittest.main()
