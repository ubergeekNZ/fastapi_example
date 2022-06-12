from typing import List, Optional
from app.models.domain.albums import Album
from app.models.schemas.rwschema import RWSchema
from pydantic import BaseModel

DEFAULT_ALBUM_LIMIT = 20
DEFAULT_ALBUM_OFFSET = 0
class ListOfAlbumsInResponse(RWSchema):
    albums: List[Album]

class AlbumInResponse(RWSchema):
    album: Album


class AlbumInCreate(RWSchema):
    album: Album

class AlbumInUpdate(BaseModel):
    album_id: Optional[int]=None
    title: Optional[str] = None
    artist_id: Optional[int]=None