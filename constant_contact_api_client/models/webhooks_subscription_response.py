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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WebhooksSubscriptionResponse(BaseModel):
    """
    WebhooksSubscriptionResponse
    """ # noqa: E501
    topic_id: Optional[StrictInt] = Field(default=None, description="Identifies the topic using an integer to indicate the type of topic.")
    hook_uri: Optional[StrictStr] = Field(default=None, description="Your webhook callback URI. Constant Contact automatically sends POST requests to this URI to notify you about the topic.")
    topic_name: Optional[StrictStr] = Field(default=None, description="The name of the topic.")
    topic_description: Optional[StrictStr] = Field(default=None, description="A description of what the topic is and when Constant Contact notifies you concerning it.")
    __properties: ClassVar[List[str]] = ["topic_id", "hook_uri", "topic_name", "topic_description"]

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
        """Create an instance of WebhooksSubscriptionResponse from a JSON string"""
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
        """Create an instance of WebhooksSubscriptionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "topic_id": obj.get("topic_id"),
            "hook_uri": obj.get("hook_uri"),
            "topic_name": obj.get("topic_name"),
            "topic_description": obj.get("topic_description")
        })
        return _obj


