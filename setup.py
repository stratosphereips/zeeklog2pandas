#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Joaquin Bogado",
    author_email='joaquinbogado@duck.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Read Zeeek/Bro log and log.gz (even broken ones) into a Pandas Dataframe.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='zeeklog2pandas',
    name='zeeklog2pandas',
    packages=find_packages(include=['zeeklog2pandas', 'zeeklog2pandas.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/stratosphereips/zeeklog2pandas',
    version='0.1.3-rc2',
    zip_safe=False,
)
