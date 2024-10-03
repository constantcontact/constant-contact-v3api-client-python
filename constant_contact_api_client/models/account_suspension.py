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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AccountSuspension(BaseModel):
    """
    AccountSuspension
    """ # noqa: E501
    suspend_plan_id: StrictInt = Field(description="Suspended plan group id.")
    suspend_plan_group_id: StrictInt = Field(description="The suspended plan group id.")
    suspend_date: Optional[datetime] = Field(default=None, description="The date when the customer will start being suspended. If omitted defaults to the current date and time and suspends the account at the next billing cycle.")
    suspend_reason_id: Optional[StrictInt] = Field(default=None, description="The reason the customer is suspended.")
    suspend_subreason_id: Optional[StrictInt] = Field(default=None, description="The subreason why the customer is suspended.")
    suspend_comment: Optional[StrictStr] = Field(default=None, description="Comment field for user suspension.")
    suspend_estimated_reactivation_date: Optional[datetime] = Field(default=None, description="Estimated date when the customer will be reactivated.")
    __properties: ClassVar[List[str]] = ["suspend_plan_id", "suspend_plan_group_id", "suspend_date", "suspend_reason_id", "suspend_subreason_id", "suspend_comment", "suspend_estimated_reactivation_date"]

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
        """Create an instance of AccountSuspension from a JSON string"""
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
        """Create an instance of AccountSuspension from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "suspend_plan_id": obj.get("suspend_plan_id"),
            "suspend_plan_group_id": obj.get("suspend_plan_group_id"),
            "suspend_date": obj.get("suspend_date"),
            "suspend_reason_id": obj.get("suspend_reason_id"),
            "suspend_subreason_id": obj.get("suspend_subreason_id"),
            "suspend_comment": obj.get("suspend_comment"),
            "suspend_estimated_reactivation_date": obj.get("suspend_estimated_reactivation_date")
        })
        return _obj


