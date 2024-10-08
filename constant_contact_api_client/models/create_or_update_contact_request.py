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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from constant_contact_api_client.models.create_or_update_contact_request_custom_fields_inner import CreateOrUpdateContactRequestCustomFieldsInner
from constant_contact_api_client.models.create_or_update_contact_request_street_address import CreateOrUpdateContactRequestStreetAddress
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateOrUpdateContactRequest(BaseModel):
    """
    CreateOrUpdateContactRequest
    """ # noqa: E501
    email_address: Annotated[str, Field(strict=True, max_length=50)] = Field(description="The email address for the contact. This method identifies each unique contact using their email address. If the email address exists in the account, this method updates the contact. If the email address is new, this method creates a new contact.")
    first_name: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="The first name of the contact.")
    last_name: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="The last name of the contact.")
    job_title: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="The job title of the contact.")
    company_name: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="The name of the company where the contact works.")
    phone_number: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="The phone number for the contact.")
    list_memberships: Annotated[List[StrictStr], Field(min_length=1, max_length=50)] = Field(description="The contact lists you want to add the contact to as an array of up to 50 contact <code>list_id</code> values. You must include at least one <code>list_id</code>.")
    custom_fields: Optional[Annotated[List[CreateOrUpdateContactRequestCustomFieldsInner], Field(max_length=50)]] = Field(default=None, description="The custom fields you want to add to the contact as an array of up to 50 custom field objects.")
    anniversary: Optional[StrictStr] = Field(default=None, description="The anniversary date for the contact. For example, this value could be the date when the contact first became a customer of an organization in Constant Contact. Valid date formats are MM/DD/YYYY, M/D/YYYY, YYYY/MM/DD, YYYY/M/D, YYYY-MM-DD, YYYY-M-D,M-D-YYYY, or M-DD-YYYY. ")
    birthday_month: Optional[StrictInt] = Field(default=None, description="The month value for the contact's birthday. Valid values are from 1 through 12. The <code>birthday_month</code> property is required if you use <code>birthday_day</code>.")
    birthday_day: Optional[StrictInt] = Field(default=None, description="The day value for the contact's birthday. Valid values are from 1 through 31. The <code>birthday_day</code> property is required if you use <code>birthday_month</code>.")
    street_address: Optional[CreateOrUpdateContactRequestStreetAddress] = None
    __properties: ClassVar[List[str]] = ["email_address", "first_name", "last_name", "job_title", "company_name", "phone_number", "list_memberships", "custom_fields", "anniversary", "birthday_month", "birthday_day", "street_address"]

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
        """Create an instance of CreateOrUpdateContactRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in custom_fields (list)
        _items = []
        if self.custom_fields:
            for _item in self.custom_fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['custom_fields'] = _items
        # override the default output from pydantic by calling `to_dict()` of street_address
        if self.street_address:
            _dict['street_address'] = self.street_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateOrUpdateContactRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email_address": obj.get("email_address"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "job_title": obj.get("job_title"),
            "company_name": obj.get("company_name"),
            "phone_number": obj.get("phone_number"),
            "list_memberships": obj.get("list_memberships"),
            "custom_fields": [CreateOrUpdateContactRequestCustomFieldsInner.from_dict(_item) for _item in obj.get("custom_fields")] if obj.get("custom_fields") is not None else None,
            "anniversary": obj.get("anniversary"),
            "birthday_month": obj.get("birthday_month"),
            "birthday_day": obj.get("birthday_day"),
            "street_address": CreateOrUpdateContactRequestStreetAddress.from_dict(obj.get("street_address")) if obj.get("street_address") is not None else None
        })
        return _obj


