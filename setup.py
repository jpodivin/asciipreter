#!/usr/bin/env python

from distutils.core import setup

setup(
    name='asciipreter',
    version='0.1',
    description='Protection against UTF-8 encoding errors.',
    author='jpodivin',
    scripts=['asciipreter/asciipreter.py'],
    license='Apache Version 2.0',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ]
)