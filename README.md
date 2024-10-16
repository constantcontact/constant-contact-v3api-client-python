# Constant Contact V3 API Python client SDK
    Swagger build version 3.0.2475

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.117
- Package version: 1.1.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

You can install directly using:

```sh
pip install git+https://github.com/constantcontact/constant-contact-v3api-client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/constantcontact/constant-contact-v3api-client-python.git`)

Then import the package:
```python
import constant_contact_api_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import constant_contact_api_client
```
## Getting Started
This example demonstrates using an access token to send a request.
> You will need to provide a valid access token to successfully send API requests.
```python
from constant_contact_api_client import Configuration, ApiException, ApiClient, EmailCampaignsApi

configuration = Configuration(access_token='eyJraW...')
api_client = ApiClient(configuration=configuration)
emails_api = EmailCampaignsApi(api_client=api_client)
try:
    emails = emails_api.get_all_email_campaigns()
except ApiException as e:
    print(e)
```
