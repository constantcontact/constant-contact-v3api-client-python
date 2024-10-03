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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from constant_contact_api_client.models.create_list_delete_activity201_response_links import CreateListDeleteActivity201ResponseLinks
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ActivityDeleteListResponse(BaseModel):
    """
    ActivityDeleteListResponse
    """ # noqa: E501
    activity_id: Optional[StrictStr] = Field(default=None, description="Unique ID for the delete list batch job.")
    state: Optional[StrictStr] = Field(default=None, description="The state of the request:  <p><ul>  <li>initialized - request has been received</li>  <li>processing - request is being processed</li>  <li>completed - job completed</li>  <li>cancelled - request was cancelled</li>  <li>failed - job failed to complete</li>  <li>timed_out - the request timed out before completing\"</li>   </ul> </p>")
    created_at: Optional[datetime] = Field(default=None, description="Date and time that the request was received, in ISO-8601 formmat.")
    updated_at: Optional[datetime] = Field(default=None, description="Date and time that the request status was updated, in ISO-8601 format.")
    percent_done: Optional[StrictInt] = Field(default=None, description="Job completion percentage")
    activity_errors: Optional[List[StrictStr]] = Field(default=None, description="Array of messages describing the errors that occurred.")
    links: Optional[CreateListDeleteActivity201ResponseLinks] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["activity_id", "state", "created_at", "updated_at", "percent_done", "activity_errors", "_links"]

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
        """Create an instance of ActivityDeleteListResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ActivityDeleteListResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "activity_id": obj.get("activity_id"),
            "state": obj.get("state"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "percent_done": obj.get("percent_done"),
            "activity_errors": obj.get("activity_errors"),
            "_links": CreateListDeleteActivity201ResponseLinks.from_dict(obj.get("_links")) if obj.get("_links") is not None else None
        })
        return _obj


