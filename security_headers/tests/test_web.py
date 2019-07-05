# -*- coding: utf-8 -*-
from httpobs.scanner.local import scan
from selenium.webdriver.firefox.webdriver import WebDriver

from django.test import LiveServerTestCase
from django.urls import reverse

from security_headers.models import FramingAllowedFrom


class LiveServerTests(LiveServerTestCase):
    def test_allow_xframe(self):
        """
        Add whitelisted domains only and verify that they appear in header on a
        per request basis.
        """
        FramingAllowedFrom.objects.create(domain="scivero.com")
        FramingAllowedFrom.objects.create(domain="testserver")
        assert FramingAllowedFrom.objects.count() == 2

        response = self.client.get("/")
        assert response.has_header("X-Frame-Options")
        assert response["X-Frame-Options"] == "allow-from testserver"

        response = self.client.get("/", HTTP_HOST="scivero.com")
        assert response.has_header("X-Frame-Options")
        assert response["X-Frame-Options"] == "allow-from scivero.com"

        response = self.client.get("/", HTTP_HOST="google.com")
        assert response.has_header("X-Frame-Options")
        assert response["X-Frame-Options"] == "deny"


class HttpObservatoryTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(HttpObservatoryTests, cls).setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    def test_http_observatory(self):
        """
        Run the Mozilla Http Observatory against local ssl server.

        Assumes ssl-enabled localhost running at 127.0.0.1:8000.  Certificate
        verification disabled to allow self-signing.
        """
        # Display report through browser
        self.selenium.get(self.live_server_url + reverse("scan", args=["heartbeat"]))
        self.assertIn("Observatory", self.selenium.find_element_by_tag_name("h1").text)

        results = scan("127.0.0.1", path="/heartbeat/", https_port="8000", verify=False)
        assert results["scan"]["score"] >= 100
