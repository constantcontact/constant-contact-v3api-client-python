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
from pydantic import BaseModel, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EmailCampaignActivityPreview(BaseModel):
    """
    EmailCampaignActivityPreview
    """ # noqa: E501
    campaign_activity_id: Optional[StrictStr] = Field(default=None, description="The unique ID for an email campaign activity.")
    from_email: Optional[StrictStr] = Field(default=None, description="The \"from email\" email header for the email campaign activity.")
    from_name: Optional[StrictStr] = Field(default=None, description="The \"from name\" email header for the email campaign activity.")
    preheader: Optional[StrictStr] = Field(default=None, description="The email preheader for the email campaign activity. Only <code>format_type</code> 3, 4, and 5 email campaign activities use the preheader property.")
    preview_html_content: Optional[StrictStr] = Field(default=None, description="An HTML preview of the email campaign activity.")
    preview_text_content: Optional[StrictStr] = Field(default=None, description="A plain text preview of the email campaign activity.")
    reply_to_email: Optional[StrictStr] = Field(default=None, description="The email \"Reply To Email\" field for the email campaign activity.")
    subject: Optional[StrictStr] = Field(default=None, description="The email \"Subject\" field for the email campaign activity.")
    __properties: ClassVar[List[str]] = ["campaign_activity_id", "from_email", "from_name", "preheader", "preview_html_content", "preview_text_content", "reply_to_email", "subject"]

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
        """Create an instance of EmailCampaignActivityPreview from a JSON string"""
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
        """Create an instance of EmailCampaignActivityPreview from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "campaign_activity_id": obj.get("campaign_activity_id"),
            "from_email": obj.get("from_email"),
            "from_name": obj.get("from_name"),
            "preheader": obj.get("preheader"),
            "preview_html_content": obj.get("preview_html_content"),
            "preview_text_content": obj.get("preview_text_content"),
            "reply_to_email": obj.get("reply_to_email"),
            "subject": obj.get("subject")
        })
        return _obj


