"""setup.py file."""
from setuptools import setup, find_packages

__author__ = 'Andreas Thienemann <andreas@bawue.net>'

with open("requirements.txt", "r") as fs:
    reqs = [r for r in fs.read().splitlines() if (len(r) > 0 and not r.startswith("#"))]

with open("README.md", "r") as fs:
    long_description = fs.read()

setup(
    name="napalm-procurve",
    version="0.6.0",
    packages=find_packages(),
    author="Andreas Thienemann",
    author_email="andreas@bawue.net",
    description="Network Automation and Programmability Abstraction Layer (NAPALM) ProCurve driver",
    long_description="ProCurve driver support for Napalm network automation.",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/ixs/napalm-procurve",
    include_package_data=True,
    zip_safe=False,
    install_requires=reqs,
)
