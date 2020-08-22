import unittest

from sasak import create_app

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app("config.TestingConfig")
        self.client = self.app.test_client()

        self.app_context = self.app.app_context()
        self.app_context.push()

    def test_proxy_image(self):
        """Valid url"""
        res = self.client.get("/28b90ada85d84940cd708014e448c27a1fccd5dc/68747470733a2f2f65766c66637472792e70726f2f676167616b")

        self.assertEqual(res.status_code, 200)

    def test_proxy_image_invalid_url(self):
        """Invalid (hex) url"""
        res = self.client.get("/28b90ada85d84940cd708014e448c27a1fccd5dc/777177717771")

        self.assertTrue("URL is not valid" in res.get_data(as_text=True))

    def test_proxy_image_invalid_hex(self):
        """Invalid hex"""
        res = self.client.get("/x/y")

        self.assertTrue("Hex is not valid" in res.get_data(as_text=True))

    def test_proxy_image_invalid_signature(self):
        """Invalid signature"""
        res = self.client.get("/c354e75bc8a34f2f24bd6041ad0764e8aea221b4/68747470733a2f2f65766c66637472792e70726f2f676167616b")

        self.assertTrue("Signature is not match" in res.get_data(as_text=True))
    
if __name__ == "__main__":
    unittest.main()
