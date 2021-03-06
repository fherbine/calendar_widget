#!/usr/bin/python
# -*- coding: utf-8 -*-
"""See README.md for package documentation."""

from setuptools import setup

from io import open
from os import path

from calendar_widget import __version__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

URL = 'https://github.com/kivy-garden/calendar_widget'

setup(
    name='calendar_widget',
    version=__version__,
    description='A calendar widget for Kivy.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=URL,
    author="Oleg Kozlov (xxblx),\
    Anthony Lobko (amelius), Félix Herbinet (fherbine)",
    author_email="xxblx.oleg@yandex.com, felix.herbinet@yahoo.com",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='Kivy kivy-garden calendar_widget',

    packages=['calendar_widget'],
    install_requires=[],
    extras_require={
        'dev': ['pytest>=3.6', 'wheel', 'pytest-cov', 'pycodestyle'],
        'travis': ['coveralls'],
    },
    package_data={},
    data_files=[],
    entry_points={},
    project_urls={
        'Bug Reports': URL + '/issues',
        'Source': URL,
    },
)
