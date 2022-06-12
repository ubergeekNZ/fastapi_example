from typing import List, Optional

from app.models.domain.playlists import Playlist
from app.models.schemas.rwschema import RWSchema
from pydantic import BaseModel


DEFAULT_PLAYLIST_LIMIT = 20
DEFAULT_PLAYLIST_OFFSET = 0
class ListOfPlaylistsInResponse(BaseModel):
    playlists: List[Playlist]

class PlaylistInResponse(RWSchema):
    playlist: Playlist


class PlaylistInCreate(RWSchema):
    playlist: Playlist

class PlaylistInUpdate(BaseModel):
    playlist_id: Optional[int]=None
    name: Optional[str] = None