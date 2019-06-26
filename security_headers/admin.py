# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import FramingAllowedFrom


@admin.register(FramingAllowedFrom)
class FramingAllowedFromAdmin(admin.ModelAdmin):
    pass
