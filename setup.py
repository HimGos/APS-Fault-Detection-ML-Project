from setuptools import find_packages, setup
from typing import List


def get_requirements()->List[str]:...


setup(
    name='sensor',
    version='0.0.1',
    author='Himanshu Goswami',
    author_email='himgos@gmail.com',
    packages = find_packages(),
    install_requires= get_requirements(),
)

