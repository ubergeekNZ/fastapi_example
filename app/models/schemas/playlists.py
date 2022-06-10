from typing import List

from app.models.domain.playlists import Playlist
from pydantic import BaseModel


class ListOfPlaylistsInResponse(BaseModel):
    playlists: List[Playlist]