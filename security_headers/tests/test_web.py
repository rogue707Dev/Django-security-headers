from __future__ import unicode_literals

from httpobs.scanner.local import scan
from selenium.webdriver.firefox.webdriver import WebDriver

from django.test import LiveServerTestCase
from django.urls import reverse
from django.utils.decorators import classproperty

from security_headers.models import FramingAllowedFrom


class WebTests(LiveServerTestCase):
    @classproperty
    def domain(cls):
        return cls.host

    @classmethod
    def setUpClass(cls):
        super(WebTests, cls).setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    def test_allow_xframe(self):
        """
        Add some allowed domains and verify that they appear in header on a
        per request basis.
        """
        FramingAllowedFrom.objects.create(domain="scivero.com")
        FramingAllowedFrom.objects.create(domain=self.domain)
        assert FramingAllowedFrom.objects.count() == 2

        self.client.get("/")

    def test_observatory(self):
        """
        Run the Mozilla Http Observatory against local ssl server.

        Assumes ssl-enabled localhost running at 127.0.0.1:8000.  Certificate
        verification disabled to allow self-signing.
        """
        results = scan("127.0.0.1", https_port="8000", verify=False)

        # Display report through browser
        self.selenium.get(self.live_server_url + reverse("scan"))

        assert results["scan"]["score"] >= 100
