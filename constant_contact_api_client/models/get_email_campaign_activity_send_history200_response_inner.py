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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetEmailCampaignActivitySendHistory200ResponseInner(BaseModel):
    """
    GetEmailCampaignActivitySendHistory200ResponseInner
    """ # noqa: E501
    send_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="Uniquely identifies each send history object using the number of times that you sent the email campaign activity as a sequence starting at <code>1</code>. For example, when you send a specific email campaign activity twice this method returns an object with a <code>send_id</code> of 1 for the first send and an object with a <code>send_id</code> of 2 for the second send. ")
    contact_list_ids: Optional[List[StrictStr]] = Field(default=None, description="The contacts lists that Constant Contact sent email campaign activity to as an array of contact <code>list_id</code> strings.")
    segment_ids: Optional[List[StrictInt]] = Field(default=None, description="The contact segments that Constant Contact sent the email campaign activity to as an array of <code>segment_id</code> integers.")
    count: Optional[StrictInt] = Field(default=None, description="The number of contacts that Constant Contact sent this email campaign activity to. This property is specific to each send history object. When you resend an email campaign activity, Constant Contact only sends it to new contacts in the contact lists or segments you are using.")
    run_date: Optional[datetime] = Field(default=None, description="The system generated date and time that Constant Contact sent the email campaign activity to contacts in ISO-8601 format.")
    send_status: Optional[StrictStr] = Field(default=None, description="The send status for the email campaign activity. Valid values are: <ul>    <li><code>COMPLETED</code>: Constant Contact successfully sent the email campaign activity.</li>   <li><code>ERRORED</code>: Constant Contact encountered an error when sending the email campaign activity.<li> </ul> ")
    reason_code: Optional[StrictInt] = Field(default=None, description="The reason why the send attempt completed or encountered an error. This method returns <code>0</code> if Constant Contact successfully sent the email campaign activity to contacts. Possible <code>reason_code</code> values are: <ul>       <li>0 — Constant Contact successfully sent the email to contacts.</li>       <li>1 — An error occurred when sending this email. Try scheduling it again, or contact <a href='http://support.constantcontact.com' target='_blank'>Customer Support</a>.</li>       <li>2 — We were unable to send the email. Please contact our <a href='http://knowledgebase.constantcontact.com/articles/KnowledgeBase/5782-contact-an-account-review-and-deliverability-specialist' target='_blank'>Account Review Team</a> for more information.</li>       <li>3 — This Constant Contact account cannot currently send emails. This can be due to billing or product expiration.</li>       <li>4 — You're not able to send the email to that many contacts. Remove contacts from the contact lists you are using or select a list with fewer contacts.</li>       <li>5 — The email is currently in staging. For more information, see the <a href='http://knowledgebase.constantcontact.com/articles/KnowledgeBase/7402-email-staging' target='_blank>Email Staging Knowledge Base article</a>.</li>       <li>6 — Constant Contact was unable to finish sending this email to all of the contacts on your list. Please contact <a href='http://support.constantcontact.com' target='_blank'>Customer Support</a> for more information.</li>       <li>7 — The email contains invalid images. This can be caused when one or more images in the email are longer available in your image library.</li>       <li>8 — The email contains a link URL that exceeds 1005 characters.</li>       <li>9 — Constant Contact was unable to verify your authenticated Sender address. Please contact <a href='http://support.constantcontact.com' target='_blank'>Customer Support</a> for more information.</li>       <li>10 — Constant Contact was unable to verify your authenticated Sender address. Please contact <a href='http://support.constantcontact.com' target='_blank'>Customer Support</a> for more information.</li>       <li>11 — This Constant Contact account cannot send survey invitations.</li>       <li>12 — Constant Contact attempted to send the email, but there were no eligible contacts to send it to. This can be caused by an invalid contact list, a contact list with no contacts, or a contact list with no new contacts during a resend. This method displays <code>reason_code</code> 12 as a send attempt with a <code>send_status</code> of COMPLETED and a <code>count</code> of 0.</li> </ul> ")
    __properties: ClassVar[List[str]] = ["send_id", "contact_list_ids", "segment_ids", "count", "run_date", "send_status", "reason_code"]

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
        """Create an instance of GetEmailCampaignActivitySendHistory200ResponseInner from a JSON string"""
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
        """Create an instance of GetEmailCampaignActivitySendHistory200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "send_id": obj.get("send_id"),
            "contact_list_ids": obj.get("contact_list_ids"),
            "segment_ids": obj.get("segment_ids"),
            "count": obj.get("count"),
            "run_date": obj.get("run_date"),
            "send_status": obj.get("send_status"),
            "reason_code": obj.get("reason_code")
        })
        return _obj


