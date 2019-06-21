from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse


def ping(request):
    return HttpResponse("Pong")


urlpatterns = (url(r"^$", ping), url(r"^admin/", admin.site.urls))
