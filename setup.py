import setuptools
from setuptools import setup
import holodex


setup(
    name="holodex",
    version=holodex.__version__,
    author="ombe1229",
    author_email="h3236516@gmail.com",
    description="Holodex api wrapper",
    license="Apache 2.0",
    packages=setuptools.find_packages(),
    long_description=open("README.md").read(),
)
