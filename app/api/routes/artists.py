from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.artist import ArtistRepository
from app.db.errors import EntityDoesNotExist
from app.models.schemas.artists import (
    ListOfArtistsInResponse,
    DEFAULT_ARTISTS_LIMIT,
    DEFAULT_ARTISTS_OFFSET
)
from app.resources import strings

router = APIRouter()

@router.get("", response_model=ListOfArtistsInResponse, name="artist:get-all")
async def get_all(
    limit: int = Query(DEFAULT_ARTISTS_LIMIT, ge=1),
    offset: int = Query(DEFAULT_ARTISTS_OFFSET, ge=0),
    artist_repo: ArtistRepository = Depends(get_repository(ArtistRepository)),
) -> ListOfArtistsInResponse:
    records = await artist_repo.get_all(limit=limit, offset=offset)
    print(records)
    return ListOfArtistsInResponse(artists=records)