#!/usr/bin/env python
from setuptools import setup
from emoticon import __version__ as version, __doc__ as description


def fread(filepath):
    with open(filepath, 'r') as f:
        return f.read()


setup(
    name='o3o.py',
    version=version,
    include_package_data=True,
    install_requires=[
        'PyYAML',
    ],
    zip_safe=False,
    py_modules=['emoticon', 'emoticon.cli', 'emoticon.main'],
    entry_points={
        'console_scripts': [
            'o3o = emoticon.cli:main',
        ]
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    license="MIT",
    description=description,
    long_description=fread('README.rst'),
    author='Kane Blueriver',
    author_email='kxxoling@gmail.com',
    url='https://github.com/kxxoling/o3o.py',
)

