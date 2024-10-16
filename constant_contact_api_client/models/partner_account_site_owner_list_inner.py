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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PartnerAccountSiteOwnerListInner(BaseModel):
    """
    PartnerAccountSiteOwnerListInner
    """ # noqa: E501
    encoded_account_id: Optional[StrictStr] = Field(default=None, description="The obfuscated ID used to uniquely identify a client account.")
    subscriber_count: Optional[StrictInt] = Field(default=None, description="The total number of subscriber contacts that are associated with a client account.")
    organization_name: Optional[StrictStr] = Field(default=None, description="The name of the organization associated with this client account.")
    site_owner_name: Optional[StrictStr] = Field(default=None, description="The user name that identifies a client account.")
    billing_status: Optional[StrictStr] = Field(default=None, description="The client's account billing status. When you first create a client account the `billing status` defaults to `Trial`. Billing status values include: <ul>   <li><code>Trial</code> - A non-paying trial client account (default value).</li>   <li><code>Open</code> - An active and paying client account.</li>   <li><code>Canceled</code> - A canceled client account.</li>   <li><code>Trial End</code> - The trial period has ended for this client account.</li> </ul>")
    last_login_date: Optional[datetime] = Field(default=None, description="The system generated date and time (ISO-8601) showing when the client last logged into their Constant Contact account. If a client has not logged into their account, the value is `null`. This property does not display in the results.")
    __properties: ClassVar[List[str]] = ["encoded_account_id", "subscriber_count", "organization_name", "site_owner_name", "billing_status", "last_login_date"]

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
        """Create an instance of PartnerAccountSiteOwnerListInner from a JSON string"""
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
                "encoded_account_id",
                "subscriber_count",
                "organization_name",
                "site_owner_name",
                "billing_status",
                "last_login_date",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PartnerAccountSiteOwnerListInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "encoded_account_id": obj.get("encoded_account_id"),
            "subscriber_count": obj.get("subscriber_count"),
            "organization_name": obj.get("organization_name"),
            "site_owner_name": obj.get("site_owner_name"),
            "billing_status": obj.get("billing_status"),
            "last_login_date": obj.get("last_login_date")
        })
        return _obj


