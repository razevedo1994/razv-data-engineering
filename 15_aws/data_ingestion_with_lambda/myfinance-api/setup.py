import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8")
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith('"', "#", "-", "git+")
    ]


setup(
    name="myfinance",
    version="0.1.0",
    description="Myfinance is a personal finance app",
    url="myfinance.io",
    python_requires=">=3.8",
    long_description="Myfinance is a personal finance app",
    long_description_content_type="text/markdown",
    author="Rodrigo Azevedo",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=read_requirements("requirements.txt"),
    entrypoint={
        "console_scripts": ["myfinance = myfinance.cli:main"]
    }
)
