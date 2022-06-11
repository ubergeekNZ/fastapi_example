from typing import List

from app.models.domain.albums import Album
from app.models.schemas.rwschema import RWSchema


DEFAULT_ALBUM_LIMIT = 20
DEFAULT_ALBUM_OFFSET = 0
class ListOfAlbumsInResponse(RWSchema):
    albums: List[Album]

class AlbumInResponse(RWSchema):
    album: Album


class AlbumInCreate(RWSchema):
    body: str