# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin

from . import views


urlpatterns = (
    url(r"^$", views.ping, name="ping"),
    url(r"^heartbeat/$", views.heartbeat, name="heartbeat"),
    url(r"^scan/$", views.scan_url, name="scan"),
    url(r"^scan/(?P<url_name>[\w-]+)/", views.scan_url, name="scan"),
    url(r"^admin/", admin.site.urls),
)
