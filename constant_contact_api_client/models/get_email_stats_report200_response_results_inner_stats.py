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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetEmailStatsReport200ResponseResultsInnerStats(BaseModel):
    """
    Key-value pairs of campaign related statistics.
    """ # noqa: E501
    em_bounces: Optional[StrictInt] = Field(default=None, description="Number of unique email bounces.")
    em_clicks: Optional[StrictInt] = Field(default=None, description="Number of unique recipients who clicked any link in the email.")
    em_clicks_all: Optional[StrictInt] = Field(default=None, description="Total number of non-unique email clicks.")
    em_clicks_all_computer: Optional[StrictInt] = Field(default=None, description="Number of non-unique email clicks on a standard desktop or laptop computer.")
    em_clicks_all_mobile: Optional[StrictInt] = Field(default=None, description="Number of non-unique email clicks on a mobile phone or similar small mobile device (e.g. iPhone).")
    em_clicks_all_tablet: Optional[StrictInt] = Field(default=None, description="Number of non-unique email clicks on a small tablet type computer (e.g. iPad).")
    em_clicks_all_other: Optional[StrictInt] = Field(default=None, description="Number of non-unique email clicks on an unknown device (e.g. Game Console or Wearable).")
    em_clicks_all_none: Optional[StrictInt] = Field(default=None, description="Number of non-unique email clicks for which the device type was not captured. This will account for any clicks prior to when device type was collected and stored.")
    em_forwards: Optional[StrictInt] = Field(default=None, description="Number of unique recipients who forwarded the email using the forward to a friend feature (not available for all types of emails).")
    em_not_opened: Optional[StrictInt] = Field(default=None, description="Number of unique recipients who did not open the email. This is calculated as follows: <code>em_not_opened</code> is equal to <code>em_sends - em_opens - em_bounces</code>. This value is reported as zero if the calculation results in a negative value.")
    em_opens: Optional[StrictInt] = Field(default=None, description="Number of unique recipients who opened the email.")
    em_opens_all: Optional[StrictInt] = Field(default=None, description="Total number of non-unique email opens.")
    em_opens_all_computer: Optional[StrictInt] = Field(default=None, description="Number of non-unique email opens on a standard desktop or laptop computer.")
    em_opens_all_mobile: Optional[StrictInt] = Field(default=None, description="Number of non-unique email opens on a mobile phone or similar small mobile device (e.g. iPhone).")
    em_opens_all_tablet: Optional[StrictInt] = Field(default=None, description="Number of non-unique email opens on a small tablet type computer (e.g. iPad).")
    em_opens_all_other: Optional[StrictInt] = Field(default=None, description="Number of non-unique email opens on an unknown device (e.g. Game Console or Wearable).")
    em_opens_all_none: Optional[StrictInt] = Field(default=None, description="Number of non-unique email opens for which the device type was not captured. This will account for any opens prior to when device type was collected and stored.")
    em_optouts: Optional[StrictInt] = Field(default=None, description="Number of unique recipients who unsubscribed due to this email.")
    em_sends: Optional[StrictInt] = Field(default=None, description="Number of unique email sends.")
    __properties: ClassVar[List[str]] = ["em_bounces", "em_clicks", "em_clicks_all", "em_clicks_all_computer", "em_clicks_all_mobile", "em_clicks_all_tablet", "em_clicks_all_other", "em_clicks_all_none", "em_forwards", "em_not_opened", "em_opens", "em_opens_all", "em_opens_all_computer", "em_opens_all_mobile", "em_opens_all_tablet", "em_opens_all_other", "em_opens_all_none", "em_optouts", "em_sends"]

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
        """Create an instance of GetEmailStatsReport200ResponseResultsInnerStats from a JSON string"""
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
        """Create an instance of GetEmailStatsReport200ResponseResultsInnerStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "em_bounces": obj.get("em_bounces"),
            "em_clicks": obj.get("em_clicks"),
            "em_clicks_all": obj.get("em_clicks_all"),
            "em_clicks_all_computer": obj.get("em_clicks_all_computer"),
            "em_clicks_all_mobile": obj.get("em_clicks_all_mobile"),
            "em_clicks_all_tablet": obj.get("em_clicks_all_tablet"),
            "em_clicks_all_other": obj.get("em_clicks_all_other"),
            "em_clicks_all_none": obj.get("em_clicks_all_none"),
            "em_forwards": obj.get("em_forwards"),
            "em_not_opened": obj.get("em_not_opened"),
            "em_opens": obj.get("em_opens"),
            "em_opens_all": obj.get("em_opens_all"),
            "em_opens_all_computer": obj.get("em_opens_all_computer"),
            "em_opens_all_mobile": obj.get("em_opens_all_mobile"),
            "em_opens_all_tablet": obj.get("em_opens_all_tablet"),
            "em_opens_all_other": obj.get("em_opens_all_other"),
            "em_opens_all_none": obj.get("em_opens_all_none"),
            "em_optouts": obj.get("em_optouts"),
            "em_sends": obj.get("em_sends")
        })
        return _obj


