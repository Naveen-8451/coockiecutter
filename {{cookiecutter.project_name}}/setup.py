import os
from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="{{cookiecutter.project_name}}",
    version="{{cookiecutter.version_number}}",
    author="Comms",
    author_email="{{cookiecutter.team_dl_email}}",
    description="Comms PySpark Starter project code base",
    install_requires=[
        "py4j==0.10.4",
        "pyspark==2.2.1",
        "pyspark_shared_libs_8451==1.0.19"
    ],
    packages=find_packages(),
)