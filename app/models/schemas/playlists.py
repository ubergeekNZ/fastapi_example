from typing import List

from app.models.domain.playlists import Playlist
from pydantic import BaseModel

DEFAULT_PLAYLIST_LIMIT = 20
DEFAULT_PLAYLIST_OFFSET = 0
class ListOfPlaylistsInResponse(BaseModel):
    playlists: List[Playlist]