#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-query",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_query"],
    install_requires=[
        "singer-python>=5.0.12",
        "requests",
    ],
    entry_points="""
    [console_scripts]
    tap-query=tap_query:main
    """,
    packages=["tap_query"],
    package_data = {
        "schemas": ["tap_query/schemas/*.json"]
    },
    include_package_data=True,
)
