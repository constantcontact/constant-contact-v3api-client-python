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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EmailLinkClickCount(BaseModel):
    """
    EmailLinkClickCount
    """ # noqa: E501
    link_url: Optional[StrictStr] = Field(default=None, description="The URL of a link in an email campaign activity. This URL is not normalized and appears the same as the URL in the email campaign activity.")
    url_id: Optional[StrictStr] = Field(default=None, description="The ID for a unique link URL in an email campaign activity.")
    unique_clicks: Optional[StrictInt] = Field(default=None, description="The number of unique contacts that clicked the link.")
    list_action: Optional[StrictStr] = Field(default=None, description="If the link uses the click segmentation feature, this property contains the action that contacts trigger when they click the link. Currently the only available action is <code>add</code>, which adds contacts that click the link to a contact list.")
    list_id: Optional[StrictStr] = Field(default=None, description="If the link uses the click segmentation feature, this property contains the contact list linked with the <code>list_action</code> property.")
    link_tag: Optional[StrictStr] = Field(default=None, description="Link tags are not currently available in email campaigns. By default, this method combines results for duplicate link URLs. Link tags will allow users to get a separate link click report for each unique <code>link_tag</code> value they use, even if URLs are not unique.")
    __properties: ClassVar[List[str]] = ["link_url", "url_id", "unique_clicks", "list_action", "list_id", "link_tag"]

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
        """Create an instance of EmailLinkClickCount from a JSON string"""
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
        """Create an instance of EmailLinkClickCount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "link_url": obj.get("link_url"),
            "url_id": obj.get("url_id"),
            "unique_clicks": obj.get("unique_clicks"),
            "list_action": obj.get("list_action"),
            "list_id": obj.get("list_id"),
            "link_tag": obj.get("link_tag")
        })
        return _obj


