# coding: utf-8

"""
    Constant Contact API v3

    Swagger build version 3.0.2475

    The version of the OpenAPI document: 1.0.117
    Contact: webservices@constantcontact.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "constant-contact-api-client"
VERSION = "1.1.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
    "oauthlib >= 3.2.2",
    "requests >=2.28.1",
    "requests-oauthlib >= 1.3.1",
]

setup(
name=NAME,
    version=VERSION,
    description="Constant Contact API v3",
    author="Constant Contact Public API",
    author_email="webservices@constantcontact.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Constant Contact API v3"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Private",
    long_description_content_type='text/markdown',
    long_description="""\
    Swagger build version 3.0.2475
    """,  # noqa: E501
    package_data={"constant_contact_api_client": ["py.typed"]},
)
