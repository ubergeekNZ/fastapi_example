from typing import List, Optional

from app.models.domain.genres import Genre
from app.models.schemas.rwschema import RWSchema
from pydantic import BaseModel


DEFAULT_GENRES_LIMIT = 20
DEFAULT_GENRES_OFFSET = 0
class ListOfGenresInResponse(BaseModel):
    genres: List[Genre]

class GenreInResponse(RWSchema):
    genre: Genre


class GenreInCreate(RWSchema):
    genre: Genre

class GenreInUpdate(BaseModel):
    genre_id: Optional[int]=None
    name: Optional[str] = None