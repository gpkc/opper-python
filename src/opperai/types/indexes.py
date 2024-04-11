import datetime
from typing import Any, Dict, List, Optional, Union

from pydantic import UUID4, BaseModel, Field


class RetrievalResponse(BaseModel):
    content: str
    metadata: Dict[str, Any]


class Document(BaseModel):
    id: Optional[int] = None
    uuid: Optional[UUID4] = None
    key: Optional[str] = None
    content: Optional[str] = Field(None, min_length=1)
    metadata: Optional[Dict[str, Any]] = None


class Index(BaseModel):
    id: int
    name: str
    created_at: datetime.datetime


class Filter(BaseModel):
    key: str
    operation: str = Field(
        ..., description="The operation to perform on the key", pattern=r"^=|!=|>|<|in$"
    )
    value: Union[str, int, float, List[Union[str, int, float]]]
