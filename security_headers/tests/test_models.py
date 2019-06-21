from django.test import TestCase

from security_headers.models import FramingAllowedFrom


class LiveTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        FramingAllowedFrom.objects.create(domain="scivero.com")

    def test_allow_xframe(self):
        assert FramingAllowedFrom.objects.count() == 1
