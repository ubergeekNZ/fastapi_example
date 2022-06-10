from typing import List
from pydantic import BaseModel, Field, validator
from app.models.domain.rwmodel import RWModel


class Album(RWModel):
    album_id: int = Field(0, alias="album_id")
    title: str
    artist_id: int