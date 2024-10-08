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
from pydantic import BaseModel, StrictStr
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EmailAddressPut(BaseModel):
    """
    The contact's email address and related properties.
    """ # noqa: E501
    address: Annotated[str, Field(strict=True, max_length=80)] = Field(description="The email address of the contact. The email address must be unique for each contact.")
    permission_to_send: Optional[StrictStr] = Field(default=None, description="Identifies the type of permission that the Constant Contact account has to send email to the contact. Types of permission: explicit, implicit, not_set, pending_confirmation, temp_hold, unsubscribed.")
    created_at: Optional[datetime] = Field(default=None, description="Date and time that the email_address was created, in ISO-8601 format. System generated.")
    updated_at: Optional[datetime] = Field(default=None, description="Date and time that the email_address was last updated, in ISO-8601 format. System generated.")
    opt_in_date: Optional[datetime] = Field(default=None, description="Date and time that the email_address was opted-in to receive email from the account, in ISO-8601 format. System generated.")
    opt_out_source: Optional[StrictStr] = Field(default=None, description="Describes the source of the unsubscribed/opt-out action: either Account or Contact. If the Contact opted-out, then the account cannot send any campaigns to this contact until the contact opts back in. If the Account, then the account can add the contact back to any lists and send to them. Displayed only if contact has been unsubscribed/opt-out.")
    opt_out_date: Optional[datetime] = Field(default=None, description="Date and time that the contact unsubscribed/opted-out of receiving email from the account, in ISO-8601 format. Displayed only if contact has been unsubscribed/opt-out. System generated.")
    opt_out_reason: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="The reason, as provided by the contact, that they unsubscribed/opted-out of receiving email campaigns.")
    confirm_status: Optional[StrictStr] = Field(default=None, description="Indicates if the contact confirmed their email address after they subscribed to receive emails. Possible values: pending, confirmed, off.")
    __properties: ClassVar[List[str]] = ["address", "permission_to_send", "created_at", "updated_at", "opt_in_date", "opt_out_source", "opt_out_date", "opt_out_reason", "confirm_status"]

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
        """Create an instance of EmailAddressPut from a JSON string"""
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
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "created_at",
                "updated_at",
                "opt_in_date",
                "opt_out_source",
                "opt_out_date",
                "confirm_status",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EmailAddressPut from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "permission_to_send": obj.get("permission_to_send"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "opt_in_date": obj.get("opt_in_date"),
            "opt_out_source": obj.get("opt_out_source"),
            "opt_out_date": obj.get("opt_out_date"),
            "opt_out_reason": obj.get("opt_out_reason"),
            "confirm_status": obj.get("confirm_status")
        })
        return _obj


