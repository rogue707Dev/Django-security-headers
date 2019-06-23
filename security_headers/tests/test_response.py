from httpobs.scanner.local import scan

from django.test import LiveServerTestCase


class FunctionalTests(LiveServerTestCase):
    def test_observatory(self):
        results = scan("localhost", http_port=str(self.server_thread.port))
        print(results)
        assert results["scan"]["score"] >= 90
