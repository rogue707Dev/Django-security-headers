from httpobs.scanner.local import scan

from django.test import LiveServerTestCase


class FunctionalTests(LiveServerTestCase):
    def test_observatory(self):
        results = scan(self.live_server_url, http_port=8000)
        print(results)
        pass
