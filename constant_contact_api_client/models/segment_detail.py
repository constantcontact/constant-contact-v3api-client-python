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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SegmentDetail(BaseModel):
    """
    SegmentDetail
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The segment's unique descriptive name.")
    segment_criteria: Optional[Annotated[str, Field(strict=True, max_length=20000)]] = Field(default=None, description="The segment's contact selection criteria formatted as single-string escaped JSON.")
    segment_id: Optional[StrictInt] = Field(default=None, description="The system generated number that uniquely identifies the segment.")
    created_at: Optional[datetime] = Field(default=None, description="The system generated date and time (ISO-8601) that the segment was created.")
    edited_at: Optional[datetime] = Field(default=None, description="The system generated date and time (ISO-8601) that the segment's <code>name</code> or <code> segment_criteria</code> was last updated.")
    __properties: ClassVar[List[str]] = ["name", "segment_criteria", "segment_id", "created_at", "edited_at"]

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
        """Create an instance of SegmentDetail from a JSON string"""
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
                "segment_id",
                "created_at",
                "edited_at",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SegmentDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "segment_criteria": obj.get("segment_criteria"),
            "segment_id": obj.get("segment_id"),
            "created_at": obj.get("created_at"),
            "edited_at": obj.get("edited_at")
        })
        return _obj


