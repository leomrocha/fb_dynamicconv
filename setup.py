#!/usr/bin/env python3

import os
import setuptools

DIR = os.path.dirname(__file__)
REQUIREMENTS = os.path.join(DIR, "requirements.txt")


with open(REQUIREMENTS) as f:
    reqs = f.read()

setuptools.setup(
    name="fb_dynamicconv",
    version="0.0.1",
    description="pytorch modeling framework and model zoo for text models",
    url="https://github.com/leomrocha/fb_dynamicconv",
    author="Facebook; Split and Installer Leo M. Rocha",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=reqs.strip().split("\n"),
)
