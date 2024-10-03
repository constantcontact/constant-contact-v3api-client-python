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
from typing_extensions import Annotated
from constant_contact_api_client.models.create_email_campaign_request_email_campaign_activities_inner_physical_address_in_footer import CreateEmailCampaignRequestEmailCampaignActivitiesInnerPhysicalAddressInFooter
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateEmailCampaignRequestEmailCampaignActivitiesInner(BaseModel):
    """
    CreateEmailCampaignRequestEmailCampaignActivitiesInner
    """ # noqa: E501
    format_type: StrictInt = Field(description="The email format you are using to create the email campaign activity. The V3 API supports creating emails using <code>format_type</code> 5 (custom code emails). ")
    from_name: Annotated[str, Field(strict=True, max_length=100)] = Field(description="The email sender's name to display for the email campaign activity.")
    from_email: Annotated[str, Field(strict=True, max_length=80)] = Field(description="The sender's email address to use for the email campaign activity. You must use a confirmed Constant Contact account email address. Make a GET call to <code>/account/emails</code> to return a collection of account emails and their confirmation status.")
    reply_to_email: Annotated[str, Field(strict=True, max_length=80)] = Field(description="The sender's email address to use if the contact replies to the email campaign activity. You must use a confirmed Constant Contact account email address. Make a GET call to <code>/account/emails</code> to return a collection of account emails and their confirmation status.")
    subject: StrictStr = Field(description="The text to display in the subject line that describes the email campaign activity.")
    preheader: Optional[StrictStr] = Field(default=None, description="The email preheader for the email campaign activity. Contacts will view your preheader as a short summary that follows the subject line in their email client. Only <code>format_type</code> 3, 4, and 5 email campaign activities use the preheader property.")
    html_content: Annotated[str, Field(strict=True, max_length=150000)] = Field(description="The HTML content for the email campaign activity. Only <code>format_type</code> 5 (custom code emails) can contain <code>html_content</code>. When creating a <code>format_type</code> 5 custom code email, make sure that you include <code>[[trackingImage]]</code> in the <code>&lt;body&gt;</code> element of your HTML. ")
    physical_address_in_footer: Optional[CreateEmailCampaignRequestEmailCampaignActivitiesInnerPhysicalAddressInFooter] = None
    __properties: ClassVar[List[str]] = ["format_type", "from_name", "from_email", "reply_to_email", "subject", "preheader", "html_content", "physical_address_in_footer"]

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
        """Create an instance of CreateEmailCampaignRequestEmailCampaignActivitiesInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of physical_address_in_footer
        if self.physical_address_in_footer:
            _dict['physical_address_in_footer'] = self.physical_address_in_footer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateEmailCampaignRequestEmailCampaignActivitiesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "format_type": obj.get("format_type"),
            "from_name": obj.get("from_name"),
            "from_email": obj.get("from_email"),
            "reply_to_email": obj.get("reply_to_email"),
            "subject": obj.get("subject"),
            "preheader": obj.get("preheader"),
            "html_content": obj.get("html_content"),
            "physical_address_in_footer": CreateEmailCampaignRequestEmailCampaignActivitiesInnerPhysicalAddressInFooter.from_dict(obj.get("physical_address_in_footer")) if obj.get("physical_address_in_footer") is not None else None
        })
        return _obj


