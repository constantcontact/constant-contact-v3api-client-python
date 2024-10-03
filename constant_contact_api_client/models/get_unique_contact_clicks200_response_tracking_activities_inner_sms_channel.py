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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetUniqueContactClicks200ResponseTrackingActivitiesInnerSmsChannel(BaseModel):
    """
    Sms channel info for this contact
    """ # noqa: E501
    country_code: Optional[StrictStr] = Field(default=None, description="The ISO country code that is associated with SMS address.")
    state: Optional[StrictStr] = Field(default=None, description="The SMS channel status:   <ul><li><code>N</code>: not_set<li>      <li><code>T</code>: temp_hold<li>      <li><code>P</code>: pending_confirmation<li>      <li><code>I</code>: implicit<li>      <li><code>E</code>: explicit<li>      <li><code>O</code>: unsubscribed<li>      <li><code>D</code>:deprecated<li></ul>")
    formatted_international: Optional[StrictStr] = Field(default=None, description="The formatted SMS number returned if the SMS <code>country_code</code> does not match the contacts <code>country_code</code>. ")
    formatted_national: Optional[StrictStr] = Field(default=None, description="The formatted SMS number returned if the SMS <code>country_code</code> matches the contacts <code>country_code</code>. ")
    __properties: ClassVar[List[str]] = ["country_code", "state", "formatted_international", "formatted_national"]

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
        """Create an instance of GetUniqueContactClicks200ResponseTrackingActivitiesInnerSmsChannel from a JSON string"""
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
        """Create an instance of GetUniqueContactClicks200ResponseTrackingActivitiesInnerSmsChannel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "country_code": obj.get("country_code"),
            "state": obj.get("state"),
            "formatted_international": obj.get("formatted_international"),
            "formatted_national": obj.get("formatted_national")
        })
        return _obj


