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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetContactById200ResponseStreetAddressesInner(BaseModel):
    """
    GetContactById200ResponseStreetAddressesInner
    """ # noqa: E501
    street_address_id: Optional[StrictStr] = Field(default=None, description="Unique ID for the street address")
    kind: StrictStr = Field(description="Describes the type of address; valid values are home, work, or other.")
    street: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Number and street of the address.")
    city: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="The name of the city where the contact lives.")
    state: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="The name of the state or province where the contact lives.")
    postal_code: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="The zip or postal code of the contact.")
    country: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="The name of the country where the contact lives.")
    created_at: Optional[datetime] = Field(default=None, description="Date and time that the street address was created, in ISO-8601 format. System generated.")
    updated_at: Optional[datetime] = Field(default=None, description="Date and time that the street address was last updated, in ISO-8601 format. System generated.")
    __properties: ClassVar[List[str]] = ["street_address_id", "kind", "street", "city", "state", "postal_code", "country", "created_at", "updated_at"]

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
        """Create an instance of GetContactById200ResponseStreetAddressesInner from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "street_address_id",
                "created_at",
                "updated_at",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetContactById200ResponseStreetAddressesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "street_address_id": obj.get("street_address_id"),
            "kind": obj.get("kind"),
            "street": obj.get("street"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "postal_code": obj.get("postal_code"),
            "country": obj.get("country"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


