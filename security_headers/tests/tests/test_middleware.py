# -*- coding: utf-8 -*-
import pytest

from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse

from security_headers.middleware import extra_security_headers_middleware


@pytest.fixture
def response(rf):
    middleware = extra_security_headers_middleware(HttpResponse)
    response = middleware(rf.get("/"))
    return response


@pytest.mark.django_db
def test_add_feature_policy(response):
    assert response.has_header("Feature-Policy")


@pytest.mark.django_db
def test_add_referrer_policy(response):
    assert response.has_header("Referrer-Policy")


@pytest.mark.django_db
def test_add_xframe_options_policy(response):
    assert response.has_header("X-Frame-Options")


@pytest.mark.django_db
def test_add_xframe_allowed_all_domains_from_settings(rf, settings):
    settings.FRAMING_ALLOWED_FROM = ["*"]
    middleware = extra_security_headers_middleware(HttpResponse)
    request = rf.get("/")
    response = middleware(request)
    assert response.has_header("X-Frame-Options")
    assert "allow-from {}".format(request.get_host()) in response["X-Frame-Options"]


@pytest.mark.django_db
def test_add_xframe_allowed_some_domains_from_settings(rf, settings):
    # Domain not in list
    settings.FRAMING_ALLOWED_FROM = ["domain-one.ca", "domain-two.ca"]
    middleware = extra_security_headers_middleware(HttpResponse)
    request = rf.get("/")
    response = middleware(request)
    assert request.get_host() not in settings.FRAMING_ALLOWED_FROM
    assert response.has_header("X-Frame-Options")
    assert "deny" in response["X-Frame-Options"]

    # Domain in list
    settings.FRAMING_ALLOWED_FROM.append(request.get_host())
    response = middleware(request)
    assert request.get_host() in settings.FRAMING_ALLOWED_FROM
    assert response.has_header("X-Frame-Options")
    assert "allow-from {}".format(request.get_host()) in response["X-Frame-Options"]


@pytest.mark.django_db
def test_add_xframe_allowed_with_string_from_settings(rf, settings):
    # Check bad configuration
    settings.FRAMING_ALLOWED_FROM = "domain-one.ca"
    middleware = extra_security_headers_middleware(HttpResponse)
    request = rf.get("/")
    pytest.raises(ImproperlyConfigured, middleware, request)
