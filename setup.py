from setuptools import setup, find_packages
from os import path, listdir

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()


setup(
    name='CUriTools',
    version='0.6',
    packages=find_packages(exclude=["curitools.tests"]),
    url='https://github.com/gutorc92/curitools',
    author='Gustavo Coelho',
    author_email='gutorc@hotmail.com',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=long_description,
    keywords='uri',
    install_requires=['requests','click','clint','bs4'],
    package_data={
        'curitools':  ["templates/*"],
    },
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': [
            'curitools=curitools.curitools:uri',
        ],
    },
    
    
)
