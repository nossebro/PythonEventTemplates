# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EventTemplates",
    version="0.0.1",
    author="nossebro",
    author_email="43040066+nossebro@users.noreply.github.com",
    description="Event Templates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SpecsNDev/PythonEventTemplates",
    project_urls={
        "Bug Tracker": "https://github.com/SpecsNDev/PythonEventTemplates/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    packages=['EventTemplates'],
    python_requires=">=2.7, !=3.*",
)
