from typing import List

from app.models.domain.tracks import Track
from pydantic import BaseModel

DEFAULT_TRACKS_LIMIT = 20
DEFAULT_TRACKS_OFFSET = 0

class ListOfTracksInResponse(BaseModel):
    tracks: List[Track]