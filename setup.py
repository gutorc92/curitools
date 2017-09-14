from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(
    name='CUriTools',
    version='0.5',
    packages=find_packages(exclude=["tests"]),
    url='https://github.com/gutorc92/uritools',
    author='Gustavo Coelho',
    author_email='gutorc@hotmail.com',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=long_description,
    keywords='uri',
    install_requires=['requests','click','clint','bs4'],
    entry_points={
        'console_scripts': [
            'curitools=curitools.curitools:uri',
        ],
    },
    
)
