from typing import List
from pydantic import BaseModel, Field, validator
from app.models.domain.rwmodel import RWModel


class MediaType(RWModel):
    media_type_id: int = Field(0, alias="media_type_id")
    name: str