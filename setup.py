from setuptools import find_packages, setup
from typing import List
# find_packages will search for folder and convert it into package to be used as library. In our case our folder is 'sensor'.
# Any folder containing __init__ file will be considered as a package for find_packages.

def get_requirements()->List[str]:...
# this function provides list of library names that is required for this project


setup(
    name='sensor',
    version='0.0.1',
    author='Himanshu Goswami',
    author_email='himgos@gmail.com',
    packages = find_packages(),
    install_requires= get_requirements(),
)

