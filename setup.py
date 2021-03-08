"""
    This is part of Kerykeion (C) 2020 Giacomo Battaglia
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="astrochart_svg",
    version="1.0.1",
    author="Giacomo Battaglia",
    author_email="battaglia.giacomo@yahoo.it",
    description="Chart SVG generator for astrology.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/g-battaglia/astrochart_svg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires='>=3.6',
    install_requires = ['kerykeion'],
)
