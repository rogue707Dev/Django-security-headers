# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin

from . import views


urlpatterns = (
    url(r"^$", views._ping),
    url(r"^scan_default/$", views._scan_default, name="scan-default"),
    url(r"^scan/$", views.scan_request, name="scan-request"),
    url(r"^admin/", admin.site.urls),
)
