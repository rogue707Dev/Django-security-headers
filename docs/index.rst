.. Django Security Headers documentation master file, created by
   sphinx-quickstart on Tue Jun 25 22:18:22 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===================================================
Welcome to Django Security Headers's documentation!
===================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents

   contents.rst


Introduction
============

Security Headers is a simple app for Django 1.11-LTS and 2.2-LTS that adds some configurable security headers to all Django responses.  It was originally inspired by Scott Helme's `securityheaders.com <https://securityheaders.com>`_ and works in parallel with the excellent `Django-CSP <https://github.com/mozilla/django-csp>`_ package by Mozilla.  It is self-tested using the `Http Observatory <https://github.com/mozilla/http-observatory>`_ (also by Mozilla).

For Django 1.11, it relies on the `django-cookies-samesite <https://github.com/jotes/django-cookies-samesite>`_ package to add the samesite flag to session and csrf cookies.  The goal of this package is to provide a basic framework for achieving an A+ grade from the Observatory.
