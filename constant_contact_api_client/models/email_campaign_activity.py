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
from constant_contact_api_client.models.get_email_campaign_activity200_response_document_properties import GetEmailCampaignActivity200ResponseDocumentProperties
from constant_contact_api_client.models.get_email_campaign_activity200_response_physical_address_in_footer import GetEmailCampaignActivity200ResponsePhysicalAddressInFooter
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EmailCampaignActivity(BaseModel):
    """
    EmailCampaignActivity
    """ # noqa: E501
    campaign_activity_id: Optional[StrictStr] = Field(default=None, description="Identifies a campaign activity in the V3 API.")
    campaign_id: Optional[StrictStr] = Field(default=None, description="Identifies a campaign in the V3 API.")
    role: Optional[StrictStr] = Field(default=None, description="The purpose of the individual campaign activity in the larger email campaign effort. Valid values are: <ul>   <li>primary_email — The main email marketing campaign that you send to contacts. The <code>primary_email</code> contains the complete email content.</li>   <li>permalink — A permanent link to a web accessible version of the <code>primary_email</code> content without any personalized email information. For example, permalinks do not contain any of the contact details that you add to the <code>primary_email</code> email content. </li>   <li>resend — An email campaign that you resend to contacts that did not open the email campaign.</li> </ul> Constant Contact creates a <code>primary_email</code> and a <code>permalink</code> role campaign activity when you create an email campaign. ")
    contact_list_ids: Optional[List[StrictStr]] = Field(default=None, description="The contacts that Constant Contact sends the email campaign activity to as an array of contact <code>list_id</code> values. You cannot use contact lists and segments at the same time in an email campaign activity.")
    segment_ids: Optional[List[StrictInt]] = Field(default=None, description="The contacts that Constant Contact sends the email campaign activity to as an array containing a single <code>segment_id</code> value. Only <code>format_type</code> 3, 4, and 5 email campaign activities support segments. You cannot use contact lists and segments at the same time in an email campaign activity.")
    current_status: Optional[StrictStr] = Field(default=None, description="The current status of the email campaign activity. Valid values are: <ul>   <li>DRAFT — An email campaign activity that you have created but have not sent to contacts.</li>   <li>SCHEDULED — An email campaign activity that you have scheduled for Constant Contact to send to contacts.</li>   <li>EXECUTING — An email campaign activity Constant Contact is currently sending to contacts. Email campaign activities are only in this status briefly.</li>   <li>DONE — An email campaign activity that you successfully sent to contacts.</li>   <li>ERROR — An email campaign activity that encountered an error.</li>   <li>REMOVED — An email campaign that a user deleted. Users can view and restore deleted emails through the UI.</li> </ul> ")
    format_type: Optional[StrictInt] = Field(default=None, description="Identifies the type of email format. Valid values are: <ul>   <li>1 - A legacy custom code email created using the V2 API, the V3 API, or the legacy UI HTML editor.</li>   <li>2 - An email created using the second generation email editor UI.</li>   <li>3 - An email created using the third generation email editor UI. This email editor features an improved drag and drop UI and mobile responsiveness.</li>   <li>4 - An email created using the fourth generation email editor UI.</li>   <li>5 - A custom code email created using the V3 API or the new UI HTML editor.</li> </ul> ")
    from_email: StrictStr = Field(description="The email \"From Email\" field for the email campaign activity. You must use a confirmed Constant Contact account email address. Make a GET call to <code>/account/emails</code> to return a collection of account emails and their confirmation status.")
    from_name: StrictStr = Field(description="The email \"From Name\" field for the email campaign activity.")
    reply_to_email: StrictStr = Field(description="The email \"Reply To Email\" field for the email campaign activity. You must use a confirmed Constant Contact account email address. Make a GET call to <code>/account/emails</code> to return a collection of account emails and their confirmation status.")
    subject: StrictStr = Field(description="The email \"Subject\" field for the email campaign activity.")
    html_content: Optional[StrictStr] = Field(default=None, description="The HTML or XHTML content for the email campaign activity. Only <code>format_type</code> 1 and 5 (legacy custom code emails or modern custom code emails) can contain <code>html_content</code>.")
    template_id: Optional[StrictStr] = Field(default=None, description="Identifies the email layout and design template that the email campaign activity is using as a base.")
    permalink_url: Optional[StrictStr] = Field(default=None, description="The permanent link to a web accessible version of the email campaign content without any personalized email information. The permalink URL becomes accessible after you send an email campaign to contacts.")
    preheader: Optional[StrictStr] = Field(default=None, description="The email preheader for the email campaign activity. Only <code>format_type</code> 3, 4, and 5 email campaign activities use the preheader property.")
    physical_address_in_footer: Optional[GetEmailCampaignActivity200ResponsePhysicalAddressInFooter] = None
    document_properties: Optional[GetEmailCampaignActivity200ResponseDocumentProperties] = None
    __properties: ClassVar[List[str]] = ["campaign_activity_id", "campaign_id", "role", "contact_list_ids", "segment_ids", "current_status", "format_type", "from_email", "from_name", "reply_to_email", "subject", "html_content", "template_id", "permalink_url", "preheader", "physical_address_in_footer", "document_properties"]

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
        """Create an instance of EmailCampaignActivity from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "campaign_activity_id",
                "campaign_id",
                "role",
                "current_status",
                "format_type",
                "template_id",
                "permalink_url",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of physical_address_in_footer
        if self.physical_address_in_footer:
            _dict['physical_address_in_footer'] = self.physical_address_in_footer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document_properties
        if self.document_properties:
            _dict['document_properties'] = self.document_properties.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EmailCampaignActivity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "campaign_activity_id": obj.get("campaign_activity_id"),
            "campaign_id": obj.get("campaign_id"),
            "role": obj.get("role"),
            "contact_list_ids": obj.get("contact_list_ids"),
            "segment_ids": obj.get("segment_ids"),
            "current_status": obj.get("current_status"),
            "format_type": obj.get("format_type"),
            "from_email": obj.get("from_email"),
            "from_name": obj.get("from_name"),
            "reply_to_email": obj.get("reply_to_email"),
            "subject": obj.get("subject"),
            "html_content": obj.get("html_content"),
            "template_id": obj.get("template_id"),
            "permalink_url": obj.get("permalink_url"),
            "preheader": obj.get("preheader"),
            "physical_address_in_footer": GetEmailCampaignActivity200ResponsePhysicalAddressInFooter.from_dict(obj.get("physical_address_in_footer")) if obj.get("physical_address_in_footer") is not None else None,
            "document_properties": GetEmailCampaignActivity200ResponseDocumentProperties.from_dict(obj.get("document_properties")) if obj.get("document_properties") is not None else None
        })
        return _obj


