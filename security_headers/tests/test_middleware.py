# Follows patterns in django-csp by Mozilla
from django.http import HttpResponse
from django.test import RequestFactory

from security_headers.middleware import extra_security_headers_middleware as m


rf = RequestFactory()


def test_add_feature_policy():
    request = rf.get("/")
    response = HttpResponse()
    new_response = m(request, response)
    assert "FEATURE_POLICY" in new_response
