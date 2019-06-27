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

Security Headers is a simple Django app (originally inspired by Scott Helme's `securityheaders.com <https://securityheaders.com>`_) that adds configurable security headers to all Django responses.  It works in parallel with the excellent `Django-CSP <https://github.com/mozilla/django-csp>`_ package and is self-tested using the `Http Observatory <https://github.com/mozilla/http-observatory>`_ both maintained by Mozilla.  The goal of this package is to provide a basic framework for achieving an A+ grade.
