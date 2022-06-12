from typing import List, Optional

from app.models.domain.tracks import Track
from app.models.schemas.rwschema import RWSchema
from pydantic import BaseModel


DEFAULT_TRACKS_LIMIT = 20
DEFAULT_TRACKS_OFFSET = 0

class ListOfTracksInResponse(BaseModel):
    tracks: List[Track]

class TrackInResponse(RWSchema):
    track: Track


class TrackInCreate(RWSchema):
    Track: Track

class TrackInUpdate(BaseModel):
    track_id: Optional[int]=None
    name: Optional[str]=None
    album_id: Optional[int]=None
    media_type_id: Optional[int]=None
    genre_id: Optional[int]=None
    composer: Optional[str] = None
    milliseconds: Optional[int]=None
    bytes: Optional[int]=None
    unit_price: Optional[float]=None