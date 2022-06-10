from typing import List

from app.models.domain.genres import Genre
from pydantic import BaseModel


class ListOfGenresInResponse(BaseModel):
    genres: List[Genre]