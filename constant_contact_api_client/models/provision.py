# coding: utf-8

"""
    Constant Contact API v3

    Swagger build version 3.0.2475

    The version of the OpenAPI document: 1.0.97
    Contact: webservices@constantcontact.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Provision(BaseModel):
    """
    Provision
    """ # noqa: E501
    contact_email: Annotated[str, Field(strict=True, max_length=80)] = Field(description="A valid email address to associate with the client account.")
    contact_phone: Optional[Annotated[str, Field(min_length=5, strict=True, max_length=25)]] = Field(default=None, description="The contact phone number to associate with the client account.")
    country_code: Annotated[str, Field(min_length=2, strict=True, max_length=3)] = Field(description="The two-letter country code (ISO 3166-1 code) that specifies the country in which the client resides.")
    organization_name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=50)]] = Field(default=None, description="The name of organization that identifies the client account.")
    organization_phone: Optional[Annotated[str, Field(min_length=5, strict=True, max_length=25)]] = Field(default=None, description="The organization phone number. To set the organization phone number using the user interface, select <b>My Settings</b> and in the <b>Organization Information</b> section, select <b>Edit Organization Information</b>.")
    state_code: StrictStr = Field(description="The two-letter state code that represents the US state (<code>country_code</code> is <code>US</code> ) or Canadian province (<code>country_code</code> is <code>CA</code>) where the client's organization is physically located. Leave the <code>state_code</code> blank for non-US states and Canadian provinces.")
    time_zone_id: Optional[StrictStr] = Field(default=None, description="The offical time zone to use to represent the physical location associated with the client account.")
    website: Optional[StrictStr] = Field(default=None, description="The client's website URL. Specifying the website URL eliminates the need for clients to provide that information. Requires a valid URL starting with http:// or https://.")
    login_name: Annotated[str, Field(min_length=6, strict=True, max_length=50)] = Field(description="A unique login name to associate with the client account. The name must only contain alphanumeric characters and '-', '_', '@','.','+'. ")
    password: Optional[Annotated[str, Field(min_length=8, strict=True, max_length=80)]] = Field(default=None, description="Required if not using Single Sign On (SSO) or external authenticator. The password to associate with the client account. Passwords must be at least 8 characters and no more than 80 characters in length. Passwords can contain alphabetical letters (A-Z) and (a-z), numbers (0-9), special characters (! @ # $ etc.) and spaces. Passwords should not contain any part of your username and cannot be the same as your last password, or be listed on an industry database; we check for easily guessed or compromised passwords. Your new password is not returned in the response payload for security reasons. If using SSO authentication, use <code>idp_provider</code> and <code>idp_provider_id</code> instead of <code>password</code>.")
    first_name: Optional[Annotated[str, Field(min_length=2, strict=True, max_length=80)]] = Field(default=None, description="The client account owner's first name.")
    last_name: Optional[Annotated[str, Field(min_length=2, strict=True, max_length=80)]] = Field(default=None, description="The client account owner's last name.")
    partner_account_id: Optional[Annotated[str, Field(strict=True, max_length=80)]] = Field(default=None, description="The unique client account identifier that partners define and use for billing and reporting purposes.")
    billing_locale: Optional[StrictStr] = Field(default=None, description="The currency to use when billing the client account. Valid values are: <code>en_US</code> (default, US Dollars) or <code>en_GB</code> (British Pounds).")
    managed_site_owner: Optional[StrictBool] = Field(default=None, description="By default, if the client account is setup as a managed account <code>managed_site_owner</code> is automatically set to <code>true</code> and attempting to override the setting with <code>false</code> is ignored. This helps to avoid getting an account into an unknown state.")
    enable_single_billing: Optional[StrictBool] = Field(default=None, description="If a partner account is setup to allow for single billing and the <code>managed_site_owner</code> property is set to <code>true</code>, use this property to enable the single billing feature for the client account. See your account manager for more information.")
    gdpr_opt_out: Optional[StrictBool] = Field(default=None, description="When creating accounts for users who have opted-out of any marketing communications, set  the <code> gdpr_opt_out</code>  to <code>true</code>  so that Constant Contact does not send any marketing communications to the account.")
    external_id: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="The ID used to uniquely identify the client account for the external authenticator. Do not use the <code>password</code> property when using an external authenticator.")
    external_provider: Optional[Annotated[str, Field(strict=True, max_length=80)]] = Field(default=None, description="The name of the provider who externally authenticates this customer. For example, PayPal or Yahoo. Do not use the <code>password</code> property when using an external authenticator.")
    __properties: ClassVar[List[str]] = ["contact_email", "contact_phone", "country_code", "organization_name", "organization_phone", "state_code", "time_zone_id", "website", "login_name", "password", "first_name", "last_name", "partner_account_id", "billing_locale", "managed_site_owner", "enable_single_billing", "gdpr_opt_out", "external_id", "external_provider"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Provision from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Provision from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contact_email": obj.get("contact_email"),
            "contact_phone": obj.get("contact_phone"),
            "country_code": obj.get("country_code"),
            "organization_name": obj.get("organization_name"),
            "organization_phone": obj.get("organization_phone"),
            "state_code": obj.get("state_code"),
            "time_zone_id": obj.get("time_zone_id"),
            "website": obj.get("website"),
            "login_name": obj.get("login_name"),
            "password": obj.get("password"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "partner_account_id": obj.get("partner_account_id"),
            "billing_locale": obj.get("billing_locale"),
            "managed_site_owner": obj.get("managed_site_owner"),
            "enable_single_billing": obj.get("enable_single_billing"),
            "gdpr_opt_out": obj.get("gdpr_opt_out"),
            "external_id": obj.get("external_id"),
            "external_provider": obj.get("external_provider")
        })
        return _obj


