import unittest

from url_guard import is_official_idm_url


class UrlGuardTests(unittest.TestCase):
    def test_accepts_official_https_url(self):
        self.assertTrue(is_official_idm_url(
            "https://www.internetdownloadmanager.com/download.html"
        ))

    def test_rejects_lookalike_and_non_https_urls(self):
        self.assertFalse(is_official_idm_url("https://idm.example/download"))
        self.assertFalse(is_official_idm_url(
            "http://www.internetdownloadmanager.com/download.html"
        ))


if __name__ == "__main__":
    unittest.main()
