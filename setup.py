# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# 具体数据参考setup.cfg
setup(
    name="Andrew",
    version="1.0",
    url='https://github.com/liudoudou86/Andrew',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    author='liudoudou86',
    author_email='543972930@qq.com',
    description='HTTP automation testing framework based on unittest.',
    packages=find_packages('src'),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=[
        "loguru>=0.5.3",
        "configparser>=5.2.0",
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
        "Flask>=2.0.2"
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        "Topic :: Software Development :: Testing",
    ]
)