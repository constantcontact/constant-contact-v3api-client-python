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
from typing_extensions import Annotated
from constant_contact_api_client.models.create_email_campaign200_response_campaign_activities_inner import CreateEmailCampaign200ResponseCampaignActivitiesInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateEmailCampaign200Response(BaseModel):
    """
    CreateEmailCampaign200Response
    """ # noqa: E501
    campaign_activities: Optional[List[CreateEmailCampaign200ResponseCampaignActivitiesInner]] = Field(default=None, description="Lists the role and unique activity ID of each campaign activity that is associated with an Email Campaign.")
    campaign_id: Optional[StrictStr] = Field(default=None, description="The unique ID used to identify the email campaign (UUID format).")
    created_at: Optional[datetime] = Field(default=None, description="The system generated date and time that this email campaign was created. This string is readonly and is in ISO-8601 format.")
    current_status: Optional[StrictStr] = Field(default=None, description="The current status of the email campaign. Valid values are: <ul>   <li>Draft — An email campaign that you have created but have not sent to contacts.</li>   <li>Scheduled — An email campaign that you have scheduled for Constant Contact to send to contacts.</li>   <li>Executing — An email campaign that Constant Contact is currently sending to contacts. Email campaign activities are only in this status briefly.</li>   <li>Done — An email campaign that you successfully sent to contacts.</li>   <li>Error — An email campaign activity that encountered an error.</li>   <li>Removed — An email campaign that a user deleted. Users can view and restore deleted emails through the UI.</li> </ul> ")
    name: Optional[Annotated[str, Field(strict=True, max_length=80)]] = Field(default=None, description="The descriptive name the user provides to identify this campaign. Campaign names must be unique for each account ID.")
    type: Optional[StrictStr] = Field(default=None, description="Identifies the type of campaign that you select when creating the campaign. Newsletter and Custom Code email campaigns are the primary types.")
    type_code: Optional[StrictInt] = Field(default=None, description="The code used to identify the email campaign `type`. <ul>   <li> 1  (Default) </li>   <li> 2  (Bulk Email) </li>   <li> 10 (Newsletter) </li>   <li> 11 (Announcement) </li>   <li> 12 (Product/Service News) </li>   <li> 14 (Business Letter) </li>   <li> 15 (Card) </li>   <li> 16 (Press release)</li>   <li> 17 (Flyer) </li>   <li> 18 (Feedback Request) </li>   <li> 19 (Ratings and Reviews) </li>   <li> 20 (Event Announcement) </li>   <li> 21 (Simple Coupon) </li>   <li> 22 (Sale Promotion) </li>   <li> 23 (Product Promotion) </li>   <li> 24 (Membership Drive) </li>   <li> 25 (Fundraiser) </li>   <li> 26 (Custom Code Email)</li>   <li> 57 (A/B Test)</li> </ul> ")
    updated_at: Optional[datetime] = Field(default=None, description="The system generated date and time showing when the campaign was last updated. This string is read only and is in ISO-8601 format.")
    __properties: ClassVar[List[str]] = ["campaign_activities", "campaign_id", "created_at", "current_status", "name", "type", "type_code", "updated_at"]

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
        """Create an instance of CreateEmailCampaign200Response from a JSON string"""
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
                "created_at",
                "updated_at",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in campaign_activities (list)
        _items = []
        if self.campaign_activities:
            for _item in self.campaign_activities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['campaign_activities'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateEmailCampaign200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "campaign_activities": [CreateEmailCampaign200ResponseCampaignActivitiesInner.from_dict(_item) for _item in obj.get("campaign_activities")] if obj.get("campaign_activities") is not None else None,
            "campaign_id": obj.get("campaign_id"),
            "created_at": obj.get("created_at"),
            "current_status": obj.get("current_status"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "type_code": obj.get("type_code"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


