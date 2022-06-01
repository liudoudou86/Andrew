# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from Andrew import __version__, __description__


setup(
    name="Andrew",
    version=__version__,
    url='https://github.com/liudoudou86/Andrew',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    author='liudoudou86',
    author_email='543972930@qq.com',
    description=__description__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[
        "loguru>=0.5.3",
        "configparser>=5.2.0",
        "requests>=2.27.1",
        "PyHamcrest>=2.0.3",
        "jsonpath>=0.82",
        "pytest>=6.2.5",
        "pytest-html>=3.1.1",
        "pytest-xdist>=2.4.0",
        "pytest-ordering>=0.6",
        "pytest-rerunfailures>=10.2",
        "allure-pytest>=2.9.45",
        "PyMySQL>=1.0.2",
        "prettytable>=3.2.0",
        "PyYAML>=6.0",
        "Flask>=2.0.2",
        "fastapi>=0.78.0",
        "uvicorn>=0.17.6"
    ],
    entry_points='''
    [console_scripts]
    api=Andrew.Cli:main
    ''',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        "Topic :: Software Development :: Testing",
    ]
)