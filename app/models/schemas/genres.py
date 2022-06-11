from typing import List

from app.models.domain.genres import Genre
from pydantic import BaseModel

DEFAULT_GENRES_LIMIT = 20
DEFAULT_GENRES_OFFSET = 0
class ListOfGenresInResponse(BaseModel):
    genres: List[Genre]