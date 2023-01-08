from setuptools import find_packages
from setuptools import setup

VERSION = "0.0.1"

setup(
    name="simple_menu",
    version=VERSION,
    author="Chris Vann",
    author_email="chrisvann01@gmail.com",
    description="A simple console menu",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.7",
    keywords=["python", "menu", "simple menu", "console menu"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
    ],
)
