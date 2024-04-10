# coding: utf-8

"""
    config-inspector

    Get the configurational status of a currently deployed product in terms of its sub     configurational items and their corresponding health

    The version of the OpenAPI document: 0.2.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DeviceResponse(BaseModel):
    """
    DeviceResponse
    """ # noqa: E501
    name: StrictStr
    deployment_status: StrictStr
    device_properties: Dict[str, Any]
    device_attributes: List[StrictStr]
    state: Optional[StrictStr] = 'Unknown'
    chart: StrictStr
    __properties: ClassVar[List[str]] = ["name", "deployment_status", "device_properties", "device_attributes", "state", "chart"]

    @field_validator('deployment_status')
    def deployment_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Running', 'Pending', 'Succeeded', 'Failed', 'Unknown']):
            raise ValueError("must be one of enum values ('Running', 'Pending', 'Succeeded', 'Failed', 'Unknown')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DeviceResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeviceResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "deployment_status": obj.get("deployment_status"),
            "device_properties": obj.get("device_properties"),
            "device_attributes": obj.get("device_attributes"),
            "state": obj.get("state") if obj.get("state") is not None else 'Unknown',
            "chart": obj.get("chart")
        })
        return _obj


