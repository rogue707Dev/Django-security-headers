from __future__ import unicode_literals

from httpobs.scanner.local import scan

from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from django.template.response import TemplateResponse


def ping(request):
    return HttpResponse("Pong")


def http_observatory(request):
    """
    Assumes ssl-enabled localhost running at 127.0.0.1:8000.  Certificate
    verification disabled to allow self-signing.
    """
    context = {}
    context["results"] = scan("127.0.0.1", https_port="8000", verify=False)
    return TemplateResponse(request, "security_headers/scan.html", context=context)


urlpatterns = (
    url(r"^$", ping),
    url(r"^scan/$", http_observatory, name="scan"),
    url(r"^admin/", admin.site.urls),
)
