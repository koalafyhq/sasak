import unittest

from sasak import create_app

from .service import check_is_proxiable, proxy_image

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app("config.TestingConfig")
        self.client = self.app.test_client()

        self.app_context = self.app.app_context()
        self.app_context.push()

    def test_check_is_proxiable_true(self):
        """Valid url"""
        expected = check_is_proxiable("https://evlfctry.pro/gagak")

        self.assertTrue(expected)

    def test_check_is_proxiable_false_length(self):
        """Image size should less than 2MB"""
        expected = check_is_proxiable("https://evlfctry.pro/big-gif")

        self.assertFalse(expected)

    def test_check_is_proxiable_false_ext(self):
        """Target url should have image extensions"""
        expected = check_is_proxiable("https://www.google.com")

        self.assertFalse(expected)

    def test_proxy_image(self):
        """Valid url"""
        expected_status_code = 200
        actual = proxy_image("https://evlfctry.pro/gagak")

        self.assertEqual(expected_status_code, actual.status_code)

    def test_proxy_image_404(self):
        """Target url is not found"""
        not_expected_status_code = 200
        actual = proxy_image("https://evlfctry.pro/8o1022hfl")
        actual_status_code = actual[1]

        self.assertNotEqual(not_expected_status_code, actual_status_code)

if __name__ == "__main__":
    unittest.main()
