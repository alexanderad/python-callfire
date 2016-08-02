# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='python-callfire',
    version='0.1.0',
    description='CallFire API thin wrapper.',
    long_description=readme,
    author='Alexander Shchapov',
    author_email='sasha@imedicare.com',
    packages=find_packages(exclude=('tests'))
)

