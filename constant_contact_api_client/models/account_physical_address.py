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
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AccountPhysicalAddress(BaseModel):
    """
    AccountPhysicalAddress
    """ # noqa: E501
    address_line1: Annotated[str, Field(min_length=1, strict=True, max_length=80)] = Field(description="Line 1 of the organization's street address.")
    address_line2: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=80)]] = Field(default=None, description="Line 2 of the organization's street address.")
    address_line3: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=80)]] = Field(default=None, description="Line 3 of the organization's street address.")
    city: StrictStr = Field(description="The city where the organization is located.")
    state_code: Optional[Annotated[str, Field(strict=True, max_length=2)]] = Field(default=None, description="The two letter ISO 3166-1 code for the organization's state and only used if the <code>country_code</code> is <code>US</code> or <code>CA</code>. If not, exclude this property from the request body.")
    state_name: Optional[StrictStr] = Field(default=None, description="Use if the state where the organization is physically located is not in the United States or Canada. If  <code>country_code</code> is  <code>US</code> or <code>CA</code>, exclude this property from the request body.")
    postal_code: Optional[StrictStr] = Field(default=None, description="The postal code address (ZIP code) of the organization. This property is required if the <code>state_code</code> is <code>US</code> or <code>CA</code>, otherwise exclude this property from the request body.")
    country_code: StrictStr = Field(description="The two letter <a href='https://en.wikipedia.org/wiki/ISO_3166-1' target='_blank'>ISO 3166-1 code</a> for the organization's country.")
    __properties: ClassVar[List[str]] = ["address_line1", "address_line2", "address_line3", "city", "state_code", "state_name", "postal_code", "country_code"]

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
        """Create an instance of AccountPhysicalAddress from a JSON string"""
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
        """Create an instance of AccountPhysicalAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address_line1": obj.get("address_line1"),
            "address_line2": obj.get("address_line2"),
            "address_line3": obj.get("address_line3"),
            "city": obj.get("city"),
            "state_code": obj.get("state_code"),
            "state_name": obj.get("state_name"),
            "postal_code": obj.get("postal_code"),
            "country_code": obj.get("country_code")
        })
        return _obj


