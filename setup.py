# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python-callfire',
    version='0.9.3',
    description='CallFire API thin wrapper.',
    long_description=readme,
    license=license,
    author='Alexander Shchapov',
    author_email='sasha@imedicare.com',
    packages=find_packages(exclude=('tests', 'swagger'))
)

