# generated by datamodel-codegen:
#   filename:  all_of_unsupported_parent_class.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel


class UnsupportedClass(BaseModel):
    __root__: Any


class Pet(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None