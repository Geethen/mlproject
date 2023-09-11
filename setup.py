from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(filename: str) -> List[str]:
    """
    Read a requirements file and return a list of its packages.
    """
    with open(filename) as f:
        requirements = f.read().splitlines()

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author = 'Geethen',
    author_email = 'geethen.singh@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)