#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='pyjavaproperties',
    version='0.0.2',
    description='This is a "fork" of https://pypi.org/project/pyjavaproperties/. I haven\'t located the original source and made some changes so that this would work on py3.',
    author='Pier-Angelo Gaetani',
    author_email='pier.gaetani@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/UltimatePancake/pyjavaproperties',
    license='LICENSE',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: PSF License',
        'Operating System :: OS Independent'
    ]
)
