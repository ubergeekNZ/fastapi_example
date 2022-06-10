from typing import List
from pydantic import BaseModel, Field, validator
from app.models.domain.rwmodel import RWModel
from typing import Optional


class Genre(RWModel):
    genre_id: Optional[int] = Field(0, alias="genre_id")
    name: str