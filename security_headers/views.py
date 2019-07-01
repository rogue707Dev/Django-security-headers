# -*- coding: utf-8 -*-
import django

from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.urls import reverse

from httpobs.scanner.local import scan


def ping(request):
    """
    Micro view for checking response headers.
    """
    return HttpResponse("Pong")


def heartbeat(request):
    """
    Micro templated view for checking some basics.
    """
    return TemplateResponse(request, "security_headers/heartbeat.html")


def scan_url(request, url_name=None):
    """
    Importable view to run Http Observatory against a request.

    Assumes:
        - a separate ssl-enabled server is running locally on 127.0.0.1:8000.
        - certificate verification should be disabled to allow self-signing.

    Intended for testing and local development use only.
    """
    try:
        path = reverse(url_name)
    except Exception:
        path = "/"

    context = {}
    context["version"] = django.get_version()
    context["url"] = "127.0.0.1" + path
    context["results"] = scan("127.0.0.1", path=path, https_port="8000", verify=False)
    return TemplateResponse(request, "security_headers/scan.html", context=context)
