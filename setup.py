#!/usr/bin/env python

import os
from setuptools import setup, find_packages


EXTRAS_REQUIRE = {
    "tests": ["pytest~=7.2", "pytest-cov~=4.0", "responses~=0.22"],
    "lint": ["mypy==0.991", "flake8~=6.0", "bandit~=1.7"],
    "docs": ["sphinx==5.3", "sphinx-rtd-theme~=1.1", "six"],
}


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    with open(file_path) as file:
        content = file.read()
    return content


setup(
    name='splitio-requests',
    version='1.2.2',
    author='Mikayel Aleksanyan',
    author_email='miko@cyberprogrammers.net',
    license='MIT',
    url='https://github.com/mik0byte/splitio-requests',
    project_urls={
        'Source': 'https://github.com/mik0byte/splitio-requests',
    },
    description='Split.io Admin API wrapper',
    long_description=read('README.rst'),
    packages=find_packages(exclude=("tests*",)),
    python_requires=">=3.7, <4",
    install_requires=['requests>=2.28,<3', 'marshmallow>=3.19,<4', 'jsonpatch>=1.32,<2'],
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
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ]
)
