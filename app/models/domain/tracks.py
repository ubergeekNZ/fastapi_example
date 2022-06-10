from typing import List
from pydantic import BaseModel, Field, validator
from app.models.domain.rwmodel import RWModel
from typing import Optional

class Track(RWModel):
    track_id: int = Field(0, alias="track_id")
    name: str
    album_id: int
    media_type_id: int
    genre_id: int
    composer: Optional[str] = None
    milliseconds: int
    bytes: int
    unit_price: float