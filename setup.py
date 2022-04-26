# -*- coding: utf-8 -*-

from setuptools import setup

# 具体数据参考setup.cfg
setup(
    name="Andrew",
    install_requires=[
        "Werkzeug >= 2.0",
        "Jinja2 >= 3.0",
        "itsdangerous >= 2.0",
        "click >= 8.0",
        "importlib-metadata >= 3.6.0; python_version < '3.10'",
    ],
    extras_require={
        "async": ["asgiref >= 3.2"],
        "dotenv": ["python-dotenv"],
    },
)