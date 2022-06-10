from typing import List

from app.models.domain.albums import Album
from pydantic import BaseModel


class ListOfAlbumsInResponse(BaseModel):
    albums: List[Album]