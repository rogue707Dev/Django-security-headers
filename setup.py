import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django_security_headers",
    version="0.0.3",
    packages=find_packages(),
    include_package_data=True,
    license="BSD License",
    description="A simple app to add configurable security headers to Django "
    "responses.",
    long_description=README,
    url="https://bitbucket.org/scivero/django-security-headers/src/master/",
    author="Scivero",
    author_email="",
    install_requires=[
        "django>=1.11",
        "django-csp",
        "httpobs @ https://github.com/jsumnerPhD/http-observatory/archive/v1.1.tar.gz#egg=httpobs-1.1",  # noqa
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
