from fastapi import APIRouter, Body, Depends, HTTPException, Query, Response
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.artist import ArtistRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.artists import Artist
from app.models.schemas.artists import (
    ListOfArtistsInResponse,
    ArtistInResponse,
    ArtistInCreate,
    ArtistInUpdate,
    DEFAULT_ARTISTS_LIMIT,
    DEFAULT_ARTISTS_OFFSET
)
from app.resources import strings
from app.api.dependencies.artist import (
    get_artist_by_id_from_path
)

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


@router.get("/{artist_id}", response_model=ArtistInResponse, name="artists:get-by-id")
async def get_by_id(
    artist: Artist = Depends(get_artist_by_id_from_path),
) -> ArtistInResponse:
    return ArtistInResponse(artist=artist)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=ArtistInResponse,
    name="artists:create-artist",
)
async def create_artist(
    artist_create: ArtistInCreate = Body(..., embed=True, alias="artist"),
    artist_repo: ArtistRepository = Depends(get_repository(ArtistRepository)),
) -> ArtistInResponse:
    artist = await artist_repo.create_artist(artist_create.artist)
    return ArtistInResponse(artist=artist)


@router.delete(
    "/{artist_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    name="artists:delete-artist",
    response_class=Response,
)
async def delete_comment_from_article(
    artist: Artist = Depends(get_artist_by_id_from_path),
    artist_repo: ArtistRepository = Depends(get_repository(ArtistRepository)),
) -> None:
    await artist_repo.delete(data=artist)

@router.put("", response_model=ArtistInResponse, name="artists:update-artist")
async def update_artist(
    artist_update: ArtistInUpdate = Body(..., embed=True, alias="artist"),
    artist_repo: ArtistRepository = Depends(get_repository(ArtistRepository)),
) -> ArtistInResponse:
    await artist_repo.update(data=artist_update.artist)
    return ArtistInResponse(artist=artist_update.artist)