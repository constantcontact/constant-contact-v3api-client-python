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
from constant_contact_api_client.models.create_list_remove_activity_request_exclude import CreateListRemoveActivityRequestExclude
from constant_contact_api_client.models.create_list_remove_activity_request_source import CreateListRemoveActivityRequestSource
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateListRemoveActivityRequest(BaseModel):
    """
    CreateListRemoveActivityRequest
    """ # noqa: E501
    source: CreateListRemoveActivityRequestSource
    exclude: Optional[CreateListRemoveActivityRequestExclude] = None
    list_ids: Annotated[List[StrictStr], Field(max_length=0)] = Field(description="Specify up to 50 target <code>list_id</code>s from which to remove contacts.")
    __properties: ClassVar[List[str]] = ["source", "exclude", "list_ids"]

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
        """Create an instance of CreateListRemoveActivityRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exclude
        if self.exclude:
            _dict['exclude'] = self.exclude.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateListRemoveActivityRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "source": CreateListRemoveActivityRequestSource.from_dict(obj.get("source")) if obj.get("source") is not None else None,
            "exclude": CreateListRemoveActivityRequestExclude.from_dict(obj.get("exclude")) if obj.get("exclude") is not None else None,
            "list_ids": obj.get("list_ids")
        })
        return _obj


