import os
from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except:
    long_description = """
        Forked from https://github.com/FaBoPlatform/FaBo9AXIS-MPU9250-Python .
        Changes are meant to enable Python 3 support. 
        Original package is called `FaBo9Axis_MPU9250`.
        Author of original package: FaBo"""

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: Apache Software License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(
    name='FaBo9Axis_MPU9250_Python3',
    version='1.0.3',
    author='RandomUser1',
    description="Fork of `FaBo9Axis_MPU9250`. This is a library for the FaBo 9AXIS I2C Brick.",
    long_description=long_description,
    url='https://github.com/piotrek-k/FaBo9AXIS-MPU9250-Python3',
    license='Apache License 2.0',
    classifiers=classifiers,
    packages=find_packages(),
    install_requires=[
        'smbus'
    ]
)
