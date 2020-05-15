# setup.py file - set up file in order to upload my pkg in pypi

from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="Climber-pkg",  # the name that you will install via pip
    version="1.0",
    author="Theda",
    author_email="charlieandban@gmail.com(opens in new tab)",
    description="a parent Athlete class and child Rockclimber class Mods 2-3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # required if using a md file for long desc
    # license="MIT",
    url="https://github.com/LambdaTheda/lambdata-Unit3",
    # keywords="",
    packages=find_packages()  # ["my_lambdata"]
)