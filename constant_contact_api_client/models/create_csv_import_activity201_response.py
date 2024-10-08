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
from constant_contact_api_client.models.create_csv_import_activity201_response_links import CreateCSVImportActivity201ResponseLinks
from constant_contact_api_client.models.create_csv_import_activity201_response_status import CreateCSVImportActivity201ResponseStatus
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateCSVImportActivity201Response(BaseModel):
    """
    Activity status for contacts_json_import and contacts_file_import activities
    """ # noqa: E501
    activity_id: Optional[StrictStr] = Field(default=None, description="Unique ID for the activity.")
    state: Optional[StrictStr] = Field(default=None, description="The state of the request:  <p><ul>    <li>initialized - request has been received</li>   <li>processing - request is being processed</li>   <li>completed - job completed</li>   <li>cancelled - request was cancelled</li>   <li>failed - job failed to complete</li>   <li>timed_out - the request timed out before completing\"</li> </ul> </p>")
    started_at: Optional[datetime] = Field(default=None, description="Timestamp showing when we began processing the activity request, in ISO-8601 format.")
    completed_at: Optional[datetime] = Field(default=None, description="Timestamp showing when we completed processing the activity, in ISO-8601 format.")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp showing when we created the activity, in ISO-8601 format.")
    updated_at: Optional[datetime] = Field(default=None, description="Timestamp showing when we last updated the activity, in ISO-8601 format.")
    source_file_name: Optional[StrictStr] = Field(default=None, description="Name of the file used for an file_import activity.")
    percent_done: Optional[StrictInt] = Field(default=None, description="Shows the percent done for an activity that we are still processing.")
    activity_errors: Optional[List[StrictStr]] = Field(default=None, description="Array of messages describing the errors that occurred.")
    status: Optional[CreateCSVImportActivity201ResponseStatus] = None
    links: Optional[CreateCSVImportActivity201ResponseLinks] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["activity_id", "state", "started_at", "completed_at", "created_at", "updated_at", "source_file_name", "percent_done", "activity_errors", "status", "_links"]

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
        """Create an instance of CreateCSVImportActivity201Response from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "activity_id",
                "started_at",
                "completed_at",
                "created_at",
                "updated_at",
                "source_file_name",
                "percent_done",
                "activity_errors",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateCSVImportActivity201Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "activity_id": obj.get("activity_id"),
            "state": obj.get("state"),
            "started_at": obj.get("started_at"),
            "completed_at": obj.get("completed_at"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "source_file_name": obj.get("source_file_name"),
            "percent_done": obj.get("percent_done"),
            "activity_errors": obj.get("activity_errors"),
            "status": CreateCSVImportActivity201ResponseStatus.from_dict(obj.get("status")) if obj.get("status") is not None else None,
            "_links": CreateCSVImportActivity201ResponseLinks.from_dict(obj.get("_links")) if obj.get("_links") is not None else None
        })
        return _obj


