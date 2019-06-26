# -*- coding: utf-8 -*-
from django.db import models


class FramingAllowedFrom(models.Model):
    """
    Domains from which framing is allowed.
    """

    domain = models.CharField(max_length=200)

    def __str__(self):
        return self.domain
