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
from pydantic import BaseModel, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ContactTrackingActivity(BaseModel):
    """
    The base contact tracking activity representing sends, opt-outs and forwards to a friend. The basic information provided includes the campaign activity ID, tracking activity type, and time the tracking activity occurred.
    """ # noqa: E501
    contact_id: StrictStr = Field(description="The contact ID.")
    campaign_activity_id: StrictStr = Field(description="The unique ID of the activity for an e-mail campaign.")
    created_time: Optional[datetime] = Field(default=None, description="The time the tracking activity occurred")
    tracking_activity_type: Optional[StrictStr] = Field(default=None, description="The types of the tracking activities included in the request. For example, sends, opens, clicks, bounces, opt-outs, or forwards.")
    campaign_activity_name: Optional[StrictStr] = Field(default=None, description="The campaign activity name.")
    __properties: ClassVar[List[str]] = ["contact_id", "campaign_activity_id", "created_time", "tracking_activity_type", "campaign_activity_name"]

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
        """Create an instance of ContactTrackingActivity from a JSON string"""
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
        """Create an instance of ContactTrackingActivity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contact_id": obj.get("contact_id"),
            "campaign_activity_id": obj.get("campaign_activity_id"),
            "created_time": obj.get("created_time"),
            "tracking_activity_type": obj.get("tracking_activity_type"),
            "campaign_activity_name": obj.get("campaign_activity_name")
        })
        return _obj


