# -*- coding: utf-8 -*-
from httpobs.scanner.local import scan

from django.http import HttpResponse
from django.template.response import TemplateResponse


def _ping(request):
    """
    Micro view for checking response headers.

    Used for testing package.
    """
    return HttpResponse("Pong")


def _scan_default(request):
    """
    Run Http Observatory scan against default localhost.

    Assumes ssl-enabled server running locally at 127.0.0.1:8000.

    Certificate verification disabled to allow self-signing.

    Used for testing package.
    """
    context = {}
    context["results"] = scan("127.0.0.1", https_port="8000", verify=False)
    return TemplateResponse(request, "security_headers/scan.html", context=context)


def scan_request(request):
    """
    Importable view to run Http Observatory against a request.
    """
    context = {}
    context["results"] = scan(
        request.get_host() + request.get_full_path(), https_port=request.get_port()
    )
    return TemplateResponse(request, "security_headers/scan.html", context=context)
