import json
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.genre import GenreRepository
from app.db.errors import EntityDoesNotExist
from app.models.schemas.genres import (
    ListOfGenresInResponse
)
from app.resources import strings

router = APIRouter()


@router.get("", response_model=ListOfGenresInResponse, name="genres:get-all")
async def get_all(
    genre_repo: GenreRepository = Depends(get_repository(GenreRepository)),
) -> ListOfGenresInResponse:
    records = await genre_repo.get_all()
    print(records)
    return ListOfGenresInResponse(genres=records)