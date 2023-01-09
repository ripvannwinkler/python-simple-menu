from setuptools import find_packages
from setuptools import setup

VERSION = "1.0.3"

with open("README.md", "utf8", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="python_simple_menu",
    version=VERSION,
    author="Chris Vann",
    author_email="chrisvann01@gmail.com",
    description="A simple console menu",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/ripvannwinkler/python-simple-menu",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.7",
    keywords=["python", "menu", "simple menu", "console menu"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
    ],
)
