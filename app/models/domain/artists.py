from typing import List
from pydantic import BaseModel, Field, validator
from app.models.domain.rwmodel import RWModel


class Artist(RWModel):
    artist_id: int = Field(0, alias="artist_id")
    name: str