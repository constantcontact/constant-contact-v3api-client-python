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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PercentsEmail(BaseModel):
    """
    PercentsEmail
    """ # noqa: E501
    bounce: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Percentage of emails sent to unique recipients that bounced.")
    click: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Percentage of recipients who opened the email who also clicked one or more links in it.")
    desktop_click: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Percentage of clicks that came from a standard desktop or laptop computer.")
    desktop_open: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Percentage of opens that came from a standard desktop or laptop computer.")
    did_not_open: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Percentage of recipients that received the email (did not bounce) but did not open it.")
    mobile_click: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Percentage of clicks that came from a mobile phone, tablet computer, or similar small mobile device (e.g. iPhone or iPad).")
    mobile_open: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Percentage of opens that came from a mobile phone, tablet computer, or similar small mobile device (e.g. iPhone or iPad).")
    open: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Percentage of recipients that received the email (did not bounce) and opened it.")
    unsubscribe: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Percentage of recipients that received the email (did not bounce) and chose to unsubscribe.")
    __properties: ClassVar[List[str]] = ["bounce", "click", "desktop_click", "desktop_open", "did_not_open", "mobile_click", "mobile_open", "open", "unsubscribe"]

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
        """Create an instance of PercentsEmail from a JSON string"""
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
        """Create an instance of PercentsEmail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bounce": obj.get("bounce"),
            "click": obj.get("click"),
            "desktop_click": obj.get("desktop_click"),
            "desktop_open": obj.get("desktop_open"),
            "did_not_open": obj.get("did_not_open"),
            "mobile_click": obj.get("mobile_click"),
            "mobile_open": obj.get("mobile_open"),
            "open": obj.get("open"),
            "unsubscribe": obj.get("unsubscribe")
        })
        return _obj


