# coding: utf-8

"""
    Constant Contact API v3

    Swagger build version 3.0.2475

    The version of the OpenAPI document: 1.0.117
    Contact: webservices@constantcontact.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from constant_contact_api_client.models.get_account_details200_response_company_logo import GetAccountDetails200ResponseCompanyLogo
from constant_contact_api_client.models.get_account_details200_response_physical_address import GetAccountDetails200ResponsePhysicalAddress
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetAccountDetails200Response(BaseModel):
    """
    GetAccountDetails200Response
    """ # noqa: E501
    contact_email: Optional[StrictStr] = Field(default=None, description="Email addresses that are associated with the Constant Contact account owner.")
    contact_phone: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="The account owner's contact phone number (up to 25 characters in length).")
    country_code: Optional[StrictStr] = Field(default=None, description="The uppercase two-letter <a href='https://en.wikipedia.org/wiki/ISO_3166-1' target='_blank'>ISO 3166-1 code</a> representing the organization's country.")
    encoded_account_id: Optional[StrictStr] = Field(default=None, description="The readOnly encoded account ID that uniquely identifies the account.")
    first_name: Optional[StrictStr] = Field(default=None, description="The account owner's first name.")
    last_name: Optional[StrictStr] = Field(default=None, description="The account owner's last name.")
    organization_name: Optional[StrictStr] = Field(default=None, description="The name of the organization that is associated with this account.")
    organization_phone: Optional[StrictStr] = Field(default=None, description="The phone number of the organization that is associated with this account.")
    state_code: Optional[StrictStr] = Field(default=None, description="The uppercase two letter <a href='https://en.wikipedia.org/wiki/ISO_3166-1' target='_blank'>ISO 3166-1 code</a> for the organization's state. This property is required if the <code>country_code</code> is US (United States).")
    time_zone_id: Optional[StrictStr] = Field(default=None, description="The time zone that is automatically set based on the <code>state_code</code> setting; as defined in the IANA time-zone database (see http://www.iana.org/time-zones).")
    website: Optional[StrictStr] = Field(default=None, description="The organization's website URL.")
    physical_address: Optional[GetAccountDetails200ResponsePhysicalAddress] = None
    company_logo: Optional[GetAccountDetails200ResponseCompanyLogo] = None
    __properties: ClassVar[List[str]] = ["contact_email", "contact_phone", "country_code", "encoded_account_id", "first_name", "last_name", "organization_name", "organization_phone", "state_code", "time_zone_id", "website", "physical_address", "company_logo"]

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
        """Create an instance of GetAccountDetails200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "encoded_account_id",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of physical_address
        if self.physical_address:
            _dict['physical_address'] = self.physical_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of company_logo
        if self.company_logo:
            _dict['company_logo'] = self.company_logo.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetAccountDetails200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contact_email": obj.get("contact_email"),
            "contact_phone": obj.get("contact_phone"),
            "country_code": obj.get("country_code"),
            "encoded_account_id": obj.get("encoded_account_id"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "organization_name": obj.get("organization_name"),
            "organization_phone": obj.get("organization_phone"),
            "state_code": obj.get("state_code"),
            "time_zone_id": obj.get("time_zone_id"),
            "website": obj.get("website"),
            "physical_address": GetAccountDetails200ResponsePhysicalAddress.from_dict(obj.get("physical_address")) if obj.get("physical_address") is not None else None,
            "company_logo": GetAccountDetails200ResponseCompanyLogo.from_dict(obj.get("company_logo")) if obj.get("company_logo") is not None else None
        })
        return _obj


