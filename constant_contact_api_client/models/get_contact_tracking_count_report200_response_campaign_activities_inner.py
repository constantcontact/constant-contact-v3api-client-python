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
from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetContactTrackingCountReport200ResponseCampaignActivitiesInner(BaseModel):
    """
    GetContactTrackingCountReport200ResponseCampaignActivitiesInner
    """ # noqa: E501
    campaign_activity_id: StrictStr = Field(description="The unique id of the activity for an e-mail campaign.")
    start_on: datetime = Field(description="The last date at which the email was sent to this contact.")
    em_bounces: StrictInt = Field(description="The number of times the email has bounced for this contact.")
    em_clicks: StrictInt = Field(description="The number of times this contact has clicked a link in this email.")
    em_forwards: StrictInt = Field(description="The number of times this contact has forwarded this email.")
    em_opens: StrictInt = Field(description="The number of times this contact has opened this email.")
    em_sends: StrictInt = Field(description="The number of times the email was sent to this contact.")
    em_unsubscribes: StrictInt = Field(description="The number of times this contact has opted out.")
    __properties: ClassVar[List[str]] = ["campaign_activity_id", "start_on", "em_bounces", "em_clicks", "em_forwards", "em_opens", "em_sends", "em_unsubscribes"]

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
        """Create an instance of GetContactTrackingCountReport200ResponseCampaignActivitiesInner from a JSON string"""
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
        """Create an instance of GetContactTrackingCountReport200ResponseCampaignActivitiesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "campaign_activity_id": obj.get("campaign_activity_id"),
            "start_on": obj.get("start_on"),
            "em_bounces": obj.get("em_bounces"),
            "em_clicks": obj.get("em_clicks"),
            "em_forwards": obj.get("em_forwards"),
            "em_opens": obj.get("em_opens"),
            "em_sends": obj.get("em_sends"),
            "em_unsubscribes": obj.get("em_unsubscribes")
        })
        return _obj


