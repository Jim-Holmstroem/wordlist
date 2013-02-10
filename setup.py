#! -*- coding:utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': '',
    'author': 'Jim Holmström <jimho@kth.se>',
    'version': '1.1c',
    'install_requires': ['scrapy','pymongo'],
    'packages': ['wordlist'],
    'scripts': [],
    'name': 'wordlist'
}

setup(**config)
