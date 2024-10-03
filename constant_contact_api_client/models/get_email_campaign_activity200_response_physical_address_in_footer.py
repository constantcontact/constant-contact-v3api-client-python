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
from pydantic import BaseModel, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetEmailCampaignActivity200ResponsePhysicalAddressInFooter(BaseModel):
    """
    The physical address of the organization that is sending the email campaign. Constant Contact displays this information to contacts in the email message footer.
    """ # noqa: E501
    address_line1: StrictStr = Field(description="Line 1 of the organization's street address.")
    address_line2: Optional[StrictStr] = Field(default=None, description="Line 2 of the organization's street address.")
    address_line3: Optional[StrictStr] = Field(default=None, description="Line 3 of the organization's street address.")
    address_optional: Optional[StrictStr] = Field(default=None, description="An optional address field for the organization. Only <code>format_type</code> 3, 4, and 5 can use this property.")
    city: Optional[StrictStr] = Field(default=None, description="The city where the organization sending the email campaign is located.")
    country_code: StrictStr = Field(description="The uppercase two letter <a href='https://en.wikipedia.org/wiki/ISO_3166-1' target='_blank'>ISO 3166-1 code</a> for the organization's country.")
    country_name: Optional[StrictStr] = Field(default=None, description="The full name of the country where the organization sending the email is located. Automatically generated using the <code>country_code</code>.")
    organization_name: StrictStr = Field(description="The name of the organization that is sending the email campaign.")
    postal_code: Optional[StrictStr] = Field(default=None, description="The postal code address (ZIP code) of the organization.")
    state_code: Optional[StrictStr] = Field(default=None, description="The uppercase two letter <a href='https://en.wikipedia.org/wiki/ISO_3166-1' target='_blank'>ISO 3166-1 code</a> for the organization's state. This property is required if the <code>country_code</code> is US (United States).")
    state_name: Optional[StrictStr] = Field(default=None, description="The full state name for a <code>state_code</code> that is inside the United States. Automatically generated using the <code>state_code</code>.")
    state_non_us_name: Optional[StrictStr] = Field(default=None, description="The full state name for a <code>state_code</code> that is outside the United States. This property is not read only.")
    __properties: ClassVar[List[str]] = ["address_line1", "address_line2", "address_line3", "address_optional", "city", "country_code", "country_name", "organization_name", "postal_code", "state_code", "state_name", "state_non_us_name"]

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
        """Create an instance of GetEmailCampaignActivity200ResponsePhysicalAddressInFooter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "country_name",
                "state_name",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetEmailCampaignActivity200ResponsePhysicalAddressInFooter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address_line1": obj.get("address_line1"),
            "address_line2": obj.get("address_line2"),
            "address_line3": obj.get("address_line3"),
            "address_optional": obj.get("address_optional"),
            "city": obj.get("city"),
            "country_code": obj.get("country_code"),
            "country_name": obj.get("country_name"),
            "organization_name": obj.get("organization_name"),
            "postal_code": obj.get("postal_code"),
            "state_code": obj.get("state_code"),
            "state_name": obj.get("state_name"),
            "state_non_us_name": obj.get("state_non_us_name")
        })
        return _obj


