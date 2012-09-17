#!/usr/bin/env python
"""
to_sentry
======

Command line tool to dump data to sentry.  

"""

from setuptools import setup


setup(
    name='to_sentry',
    version='0.0.1',
    author='Adam DePrince',
    author_email='adeprince@nypublicradio.org',
    description='Simple command line driven logging for sentry.',
    long_description=__doc__,
    py_modules = [
        "to_sentry",
        "to_sentry/config_parser",
        "to_sentry/transmitter",
        ],
    zip_safe=True,
    license='BSD',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
    scripts = ["scripts/tosentry",],
    url = "https://github.com/adamdeprince/to_sentry",
    install_requires = [
        'raven',
        ]
)

