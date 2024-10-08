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
from pydantic import BaseModel
from pydantic import Field
from constant_contact_api_client.models.get_email_campaign_xrefs200_response_xrefs_inner import GetEmailCampaignXrefs200ResponseXrefsInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetEmailCampaignXrefs200Response(BaseModel):
    """
    GetEmailCampaignXrefs200Response
    """ # noqa: E501
    xrefs: Optional[List[GetEmailCampaignXrefs200ResponseXrefsInner]] = Field(default=None, description="An array of objects that contain a <code>v2_email_campaign_id</code> cross-referenced with a V3 <code>campaign_id</code> and a V3 <code>campaign_activity_id</code> value.")
    __properties: ClassVar[List[str]] = ["xrefs"]

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
        """Create an instance of GetEmailCampaignXrefs200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in xrefs (list)
        _items = []
        if self.xrefs:
            for _item in self.xrefs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['xrefs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetEmailCampaignXrefs200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "xrefs": [GetEmailCampaignXrefs200ResponseXrefsInner.from_dict(_item) for _item in obj.get("xrefs")] if obj.get("xrefs") is not None else None
        })
        return _obj


