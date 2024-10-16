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

class HistoryDetails(BaseModel):
    """
    Additional details about the SMS consent actions (opt-in, opt-out) in JSON format. The  <code>consent_action_type</code> and the method used to add or update a contacts SMS details determines which properties are returned in the results.
    """ # noqa: E501
    state: Optional[StrictStr] = Field(default=None, description="The code representing the consent state, including <code>E</code> for optin and <code>O</code> for Optin.")
    source: Optional[StrictStr] = Field(default=None, description="The code representing the consent source type, including <code>A</code> for Account, <code>C</code> for Contact, and <code>S</code>' for System.")
    consent_type: Optional[StrictStr] = Field(default=None, description="The type of SMS consent used.")
    consent_action_time: Optional[datetime] = Field(default=None, description="The date and time that SMS engagement data was last updated, in ISO-8601 format. System generated.")
    consent_action_type: Optional[StrictStr] = Field(default=None, description="The type of consent action provided.")
    consent_medium_type: Optional[StrictStr] = Field(default=None, description="The code representing the medium used to provide consent. Medium types include mobile device (<code>MD</code>). lead generation form(<code>LF</code>), deactivation by carrier(<code>CD</code>), import_file:(<code>FI</code>), and system (<code>SY</code>).")
    source_consent_timestamp: Optional[StrictStr] = Field(default=None, description="The time that SMS consent was last updated.")
    source_ip: Optional[StrictStr] = Field(default=None, description="If applicable, the IP address from which the consent came.")
    source_sms_number: Optional[StrictStr] = Field(default=None, description="If applicable, the SMS consent number associated with the source.")
    advertised_frequency: Optional[StrictInt] = Field(default=None, description="If applicable, the advertising numeric component used to advertise to the contact.. For example, if <code>advertised_frequency</code> is set to <code> 2</code> , and  <code>advertised_interval</code> is set to <code>M</code>, the contact receives advertisements twice a month.")
    advertised_interval: Optional[StrictStr] = Field(default=None, description="If applicable, the interval component used to advertise to the contact. For example, if <code>advertised_frequency</code> is set to <code> 2</code> , and  <code>advertised_interval</code> is set to <code>M</code>, the contact receives advertisements twice a month.")
    __properties: ClassVar[List[str]] = ["state", "source", "consent_type", "consent_action_time", "consent_action_type", "consent_medium_type", "source_consent_timestamp", "source_ip", "source_sms_number", "advertised_frequency", "advertised_interval"]

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
        """Create an instance of HistoryDetails from a JSON string"""
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
        """Create an instance of HistoryDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "state": obj.get("state"),
            "source": obj.get("source"),
            "consent_type": obj.get("consent_type"),
            "consent_action_time": obj.get("consent_action_time"),
            "consent_action_type": obj.get("consent_action_type"),
            "consent_medium_type": obj.get("consent_medium_type"),
            "source_consent_timestamp": obj.get("source_consent_timestamp"),
            "source_ip": obj.get("source_ip"),
            "source_sms_number": obj.get("source_sms_number"),
            "advertised_frequency": obj.get("advertised_frequency"),
            "advertised_interval": obj.get("advertised_interval")
        })
        return _obj


