# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

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
