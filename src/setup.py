from setuptools import find_packages, setup

_PACKAGE_DATA = {package: ["py.typed"] for package in find_packages()}

setup(
    name="zombie_diplo",
    version="0.1",
    description="Triggers and settings for the Zombie Diplo custom map.",
    url="https://github.com/sethmachine/zombie-diplo-starcraft",
    author="",
    author_email="",
    license="MIT",
    install_requires=[],
    package_data=_PACKAGE_DATA,
    packages=find_packages(),
    zip_safe=False,
)
