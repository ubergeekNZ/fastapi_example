from typing import List, Optional
from app.models.domain.artists import Artist
from app.models.schemas.rwschema import RWSchema
from pydantic import BaseModel


DEFAULT_ARTISTS_LIMIT = 20
DEFAULT_ARTISTS_OFFSET = 0
class ListOfArtistsInResponse(BaseModel):
    artists: List[Artist]

class ArtistInResponse(RWSchema):
    artist: Artist


class ArtistInCreate(RWSchema):
    artist: Artist

class ArtistInUpdate(BaseModel):
    artist_id: Optional[int]=None
    name: Optional[str] = None
