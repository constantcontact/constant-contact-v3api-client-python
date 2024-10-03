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
from pydantic import BaseModel
from pydantic import Field
from constant_contact_api_client.models.get_all_email_campaigns200_response_campaigns_inner import GetAllEmailCampaigns200ResponseCampaignsInner
from constant_contact_api_client.models.get_all_email_campaigns200_response_links import GetAllEmailCampaigns200ResponseLinks
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetAllEmailCampaigns200Response(BaseModel):
    """
    GetAllEmailCampaigns200Response
    """ # noqa: E501
    links: Optional[GetAllEmailCampaigns200ResponseLinks] = Field(default=None, alias="_links")
    campaigns: Optional[List[GetAllEmailCampaigns200ResponseCampaignsInner]] = None
    __properties: ClassVar[List[str]] = ["_links", "campaigns"]

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
        """Create an instance of GetAllEmailCampaigns200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in campaigns (list)
        _items = []
        if self.campaigns:
            for _item in self.campaigns:
                if _item:
                    _items.append(_item.to_dict())
            _dict['campaigns'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetAllEmailCampaigns200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_links": GetAllEmailCampaigns200ResponseLinks.from_dict(obj.get("_links")) if obj.get("_links") is not None else None,
            "campaigns": [GetAllEmailCampaigns200ResponseCampaignsInner.from_dict(_item) for _item in obj.get("campaigns")] if obj.get("campaigns") is not None else None
        })
        return _obj


