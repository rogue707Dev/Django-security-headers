import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="security_headers",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    license="BSD License",
    description="A simple app to add configurable security headers to Django "
    "responses.",
    long_description=README,
    url="https://django-security-headers.readthedocs.io/en/latest/",
    author="Scivero",
    author_email="",
    install_requires=["django-csp"],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11.20",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
