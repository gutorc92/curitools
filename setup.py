from setuptools import setup

setup(
    name='UriTools',
    version='0.1dev',
    packages=['uritools',],
    url='https://github.com/gutorc92/uritools',
    author='Gustavo Coelho',
    author_email='gutorc@hotmail.com',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    install_requires=['selenium','click','clint'],
)
