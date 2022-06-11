from typing import List

from app.models.domain.artists import Artist
from pydantic import BaseModel

DEFAULT_ARTISTS_LIMIT = 20
DEFAULT_ARTISTS_OFFSET = 0
class ListOfArtistsInResponse(BaseModel):
    artists: List[Artist]