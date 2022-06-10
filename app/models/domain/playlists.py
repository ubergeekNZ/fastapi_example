from typing import List
from pydantic import BaseModel, Field, validator
from app.models.domain.rwmodel import RWModel


class Playlist(RWModel):
    playlist_id: int = Field(0, alias="playlist_id")
    name: str