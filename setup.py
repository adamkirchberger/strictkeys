from setuptools import setup
import os
import sys

setup(
    name='strictkeys',
    version='1.0.0',
    description='Tool to manage rules for enforcing allowed variables in YAML and JSON files.',
    scripts=['bin/strictkeys'],
    python_requires='>=2.7',
    install_requires=['pyyaml'],
)
