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
from pydantic import BaseModel, StrictInt
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ContactsCounts(BaseModel):
    """
    ContactsCounts
    """ # noqa: E501
    total: Optional[StrictInt] = Field(default=None, description="Total number of contacts for the account.")
    explicit: Optional[StrictInt] = Field(default=None, description="Total number of contacts explicitly confirmed. Consent is obtained when you explicitly ask your potential contacts for permission to send the email (for example, using a sign-up form) and they agree. After you obtain express consent, it is good forever or until the contact opts out.")
    implicit: Optional[StrictInt] = Field(default=None, description="Total number of contacts implicitly confirmed. Consent is inferred based on actions, such as having an existing business relationship (making a purchase or donation, for example). In order to maintain implied consent to comply with CASL a contact must take a business action with you at least once every two years. Under CAN-Spam there is no need to maintain implied consent, it is assumed until the receiver indicates they no longer wish to receive messages.")
    pending: Optional[StrictInt] = Field(default=None, description="Total number of contacts pending confirmation. Consent is requested and pending confirmation from the contact.")
    unsubscribed: Optional[StrictInt] = Field(default=None, description="Total number of unsubscribed contacts. Consent is revoked when a contact has unsubscribed.")
    new_subscriber: Optional[StrictInt] = Field(default=None, description="Total number of newly subscribed contacts.")
    __properties: ClassVar[List[str]] = ["total", "explicit", "implicit", "pending", "unsubscribed", "new_subscriber"]

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
        """Create an instance of ContactsCounts from a JSON string"""
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
        """Create an instance of ContactsCounts from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "total": obj.get("total"),
            "explicit": obj.get("explicit"),
            "implicit": obj.get("implicit"),
            "pending": obj.get("pending"),
            "unsubscribed": obj.get("unsubscribed"),
            "new_subscriber": obj.get("new_subscriber")
        })
        return _obj


