import sys
from setuptools import setup, find_packages

NAME = "API"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="Isla - Token API",
    author_email="enzo.dardaillon@mines-ales.org",
    url="0.0.0.0",
    keywords=["OpenAPI", "Isla - Token API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['API=API.__main__:main']},
    long_description="""\
    Cette API gère les tokens du projet Isla.
    """
)

