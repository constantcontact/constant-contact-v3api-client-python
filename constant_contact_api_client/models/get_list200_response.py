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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetList200Response(BaseModel):
    """
    GetList200Response
    """ # noqa: E501
    list_id: StrictStr = Field(description="Unique ID for the contact list")
    name: StrictStr = Field(description="The name given to the contact list")
    description: Optional[StrictStr] = Field(default=None, description="Text describing the list.")
    favorite: Optional[StrictBool] = Field(default=False, description="Identifies whether or not the account has favorited the contact list.")
    created_at: Optional[datetime] = Field(default=None, description="System generated date and time that the resource was created, in ISO-8601 format.")
    updated_at: Optional[datetime] = Field(default=None, description="Date and time that the list was last updated, in ISO-8601 format. System generated.")
    deleted_at: Optional[datetime] = Field(default=None, description="If the list was deleted, this property shows the date and time it was deleted, in ISO-8601 format. System generated.")
    membership_count: Optional[StrictInt] = Field(default=None, description="The total number of contacts that are members in a list. Does not apply to segment type lists.")
    __properties: ClassVar[List[str]] = ["list_id", "name", "description", "favorite", "created_at", "updated_at", "deleted_at", "membership_count"]

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
        """Create an instance of GetList200Response from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "list_id",
                "created_at",
                "updated_at",
                "deleted_at",
                "membership_count",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetList200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "list_id": obj.get("list_id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "favorite": obj.get("favorite") if obj.get("favorite") is not None else False,
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "deleted_at": obj.get("deleted_at"),
            "membership_count": obj.get("membership_count")
        })
        return _obj


