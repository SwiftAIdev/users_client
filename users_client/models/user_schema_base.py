# coding: utf-8

"""
    SwiftAI - User Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UserSchemaBase(BaseModel):
    """
    UserSchemaBase
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID пользователя в системе")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = Field(default=None, description="Дата последнего обновления")
    is_delete: Optional[StrictBool] = False
    surname: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    domain: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    invite_code: Optional[StrictStr] = ''
    third_party_id: Optional[StrictStr] = Field(alias="third_party_ID")
    is_active: Optional[StrictBool] = True
    is_integrator: Optional[StrictBool] = False
    is_superuser: Optional[StrictBool] = False
    is_verified: Optional[StrictBool] = False
    __properties: ClassVar[List[str]] = ["id", "created_at", "updated_at", "is_delete", "surname", "name", "domain", "email", "invite_code", "third_party_ID", "is_active", "is_integrator", "is_superuser", "is_verified"]

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
        """Create an instance of UserSchemaBase from a JSON string"""
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
        # set to None if surname (nullable) is None
        # and model_fields_set contains the field
        if self.surname is None and "surname" in self.model_fields_set:
            _dict['surname'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if third_party_id (nullable) is None
        # and model_fields_set contains the field
        if self.third_party_id is None and "third_party_id" in self.model_fields_set:
            _dict['third_party_ID'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserSchemaBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "is_delete": obj.get("is_delete") if obj.get("is_delete") is not None else False,
            "surname": obj.get("surname"),
            "name": obj.get("name"),
            "domain": obj.get("domain"),
            "email": obj.get("email"),
            "invite_code": obj.get("invite_code") if obj.get("invite_code") is not None else '',
            "third_party_ID": obj.get("third_party_ID"),
            "is_active": obj.get("is_active") if obj.get("is_active") is not None else True,
            "is_integrator": obj.get("is_integrator") if obj.get("is_integrator") is not None else False,
            "is_superuser": obj.get("is_superuser") if obj.get("is_superuser") is not None else False,
            "is_verified": obj.get("is_verified") if obj.get("is_verified") is not None else False
        })
        return _obj


