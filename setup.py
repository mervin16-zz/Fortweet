from setuptools import find_packages
from setuptools import setup

setup(
    name="app",
    version="1.0.0",
    url="",
    maintainer="th3pl4gu3",
    maintainer_email="th3pl4gu33@gmail.com",
    description="Fortweet",
    long_description="The Fortweet project consists of a Dynamic Web App and a Static API which capture live tweets of Twitter, for a certain amount of time, about the online Battle Royale game Fortnite. This repo consists solely of the Static API.",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"],
    extras_require={"test": ["pytest"]},
)
