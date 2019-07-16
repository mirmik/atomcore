#!/usr/bin/env python3

from wheel.bdist_wheel import bdist_wheel as bdist_wheel_
from setuptools import setup, Extension, Command
from distutils.util import get_platform

import glob
import sys
import os

setup(
    name="atomcore",
    packages=["atomcore"],
    version="0.0.1",
    license="UNLICENSED",
    description="ATOMCORE",
    author="mirmik",
    author_email="netricks@protonmail.com",
    url="https://github.com/mirmik/atomcore",
    classifiers=[],
    include_package_data=True,
    install_requires=[],
    entry_points={"console_scripts": ["atomcore=atomcore.__main__:main"]},
)
