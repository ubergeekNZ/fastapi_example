from typing import List

from app.models.domain.artists import Artist
from pydantic import BaseModel


class ListOfArtistsInResponse(BaseModel):
    artists: List[Artist]