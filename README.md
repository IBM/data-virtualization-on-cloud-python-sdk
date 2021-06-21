# IBM Data Virtualization on Cloud Python SDK
A Python client library to interact with
the [IBM Data Virtualization on Cloud APIs](https://cloud.ibm.com/apidocs/data-virtualization-on-cloud).

<details>
<summary>Table of Contents</summary>

- [IBM Data Virtualization on Cloud Python SDK](#ibm-data-virtualization-on-cloud-python-sdk)
  - [Overview](#overview)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Authentication](#authentication)
    - [Examples](#examples)
      - [Programmatic credentials](#programmatic-credentials)
  - [Using the SDK](#using-the-sdk)
    - [Basic usage](#basic-usage)
  - [Questions](#questions)
  - [Issues](#issues)
  - [Open source @ IBM](#open-source--ibm)
  - [Contributing](#contributing)
  - [License](#license)

</details>

## Overview

The IBM Data Virtualization on Cloud Python SDK allows developers to programmatically interact with the following IBM Cloud services:

Service Name | Package name 
--- | --- 
[Data Virtualization](https://cloud.ibm.com/apidocs/data-virtualization-on-cloud-python-sdk) | datavirtualizationv1

## Prerequisites

[ibm-cloud-onboarding]: https://cloud.ibm.com/registration
* An [IBM Cloud][ibm-cloud-onboarding] account.
* An IAM API key to allow the SDK to access your account. Create one [here](https://cloud.ibm.com/iam/apikeys).
- Python 3.5.3 or above.

## Installation

To install, use `pip` or `easy_install`:

```bash
pip install --upgrade "ibm-data-virtualization-on-cloud-python-sdk"
```

or

```bash
easy_install --upgrade "ibm-data-virtualization-on-cloud-python-sdk"
```

## Authentication

Data Virtualization uses token-based Identity and Access Management (IAM) authentication.

With IAM authentication, you supply an API key that is used to generate an access token. Then, the access token is
included in each API request to Data Virtualization. Access tokens are valid for a limited amount of time and must be
regenerated.

Authentication for this SDK is accomplished by
using [IAM authenticators](https://github.com/IBM/ibm-cloud-sdk-common/blob/master/README.md#authentication). Import
authenticators from `ibm_cloud_sdk_core.authenticators`.

### Examples

#### Programmatic credentials

```python
from ibm_cloud_sdk_core.authenticators.iam_authenticator import IAMAuthenticator

dataVirtualization = dataVirtualizationV1(
    authenticator=IAMAuthenticator(apikey='<IBM_CLOUD_API_KEY>')
)
```

To learn more about IAM authenticators and how to use them in your Python application, see
the [IBM Python SDK Core documentation](https://github.com/IBM/python-sdk-core/blob/master/Authentication.md).

## Using the SDK
For general SDK usage information, please see [this link](https://github.com/IBM/ibm-cloud-sdk-common/blob/main/README.md)

### Basic usage

- Use the `set_service_url` method to set the endpoint URL that is specific to your Data Virtualization service instance.


## Questions

If you are having difficulties using this SDK or have a question about the IBM Cloud services,
please ask a question at 
[Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-cloud).

## Issues
If you encounter an issue with the project, you are welcome to submit a
[bug report](https://github.com/IBM/data-virtualization-on-cloud-python-sdk/issues).
Before that, please search for similar issues. It's possible that someone has already reported the problem.

## Open source @ IBM
Find more open source projects on the [IBM Github Page](http://ibm.github.io/)

## Contributing
See [CONTRIBUTING](CONTRIBUTING.md).

## License

This SDK project is released under the Apache 2.0 license.
The license's full text can be found in [LICENSE](LICENSE).
