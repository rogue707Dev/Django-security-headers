import pprint
from httpobs.scanner.local import scan

from django.test import LiveServerTestCase


class FunctionalTests(LiveServerTestCase):
    def test_observatory(self):
        results = scan("127.0.0.1", https_port="8000", verify=False)
        pprint.pprint(results)
        assert results["scan"]["score"] >= 90
