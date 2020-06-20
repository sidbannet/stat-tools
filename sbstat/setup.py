"""Setup of the the sbstat package.

setup file for this Python project.
Author: Siddhartha Banerjee [sidban@uwalumni.com]

"""

from setuptools import setup, find_namespace_packages

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="stat-tools",
    version="0.2",
    description="Statistical tool namespace package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="statistics data analysis",
    packages=find_namespace_packages(include=['sbstat.*']),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=["docutils>=0.3"],

    # metadata to display on PyPI
    author="Siddhartha Banerjee",
    author_email="sidban@uwalumni.com",
    url="https://github.com/sidbannet/stat-tools",   # project home page
    project_urls={
        "Bug Tracker": "https://github.com/sidbannet/stat-tools",
        "Documentation": "https://github.com/sidbannet/stat-tools",
        "Source Code": "https://github.com/sidbannet/stat-tools",
    },
    license="OSI Approved :: GNU General Public License v3 (GPLv3)",
    classifiers=[
        "License :: GNU General Public License v3.0 ",
    ]
    # could also include long_description, download_url, etc.
)
