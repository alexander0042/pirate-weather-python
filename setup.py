import os

from setuptools import find_packages, setup

__version__ = "0.0.9"


with open(os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "README.md")
) as f:
    README = f.read()

repo_url = "https://github.com/bakobako/pirate-weather-python"
setup(
    version=__version__,
    name="pirate-weather-python",
    packages=find_packages(),
    install_requires=["requests==2.21.0", "pytz==2019.1", "aiohttp==3.8.5"],
    description="The Pirate Weather API wrapper",
    long_description="View on github",
    author="bakobako",
    author_email="adam.bako@keboola.com",
    url=repo_url,
    download_url=f"{repo_url}/archive/{__version__}.tar.gz",
    license="GPLv3 License",
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
