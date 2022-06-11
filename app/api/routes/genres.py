import json
from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.genre import GenreRepository
from app.db.errors import EntityDoesNotExist
from app.models.schemas.genres import (
    ListOfGenresInResponse,
    DEFAULT_GENRES_LIMIT,
    DEFAULT_GENRES_OFFSET
)
from app.resources import strings

router = APIRouter()


@router.get("", response_model=ListOfGenresInResponse, name="genres:get-all")
async def get_all(
    limit: int = Query(DEFAULT_GENRES_LIMIT, ge=1),
    offset: int = Query(DEFAULT_GENRES_OFFSET, ge=0),
    genre_repo: GenreRepository = Depends(get_repository(GenreRepository)),
) -> ListOfGenresInResponse:
    records = await genre_repo.get_all(limit=limit, offset=offset)
    print(records)
    return ListOfGenresInResponse(genres=records)