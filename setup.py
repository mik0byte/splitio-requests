#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


EXTRAS_REQUIRE = {
    "tests": ["pytest~=6.1", "pytest-cov~=2.10", "responses~=0.12"],
    "lint": ["mypy==0.790", "flake8~=3.8", "bandit~=1.6"],
    "docs": ["sphinx==3.3.1", "sphinx-rtd-theme~=0.5"],
}


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    with open(file_path) as file:
        content = file.read()
    return content


setup(
    name='splitio-requests',
    version='1.1.1',
    author='Mikayel Aleksanyan',
    author_email='miko@cyberprogrammers.net',
    license='MIT',
    url='https://github.com/mikoblog/splitio-requests',
    project_urls={
        'Source': 'https://github.com/mikoblog/splitio-requests',
    },
    description='Split.io Admin API wrapper',
    long_description=read('README.rst'),
    packages=find_packages(exclude=("tests*",)),
    python_requires=">=3.6, <4",
    install_requires=['requests>=2.23,<3', 'marshmallow>=3.6,<4',
                      'jsonpatch>=1.25,<2', 'dataclasses==0.7;python_version<"3.7"'],
    extras_require=EXTRAS_REQUIRE,
    test_suite="tests",
    keywords=[
        "Split.io",
        "split",
        "API wrapper",
        "api",
        "requests",
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ]
)
