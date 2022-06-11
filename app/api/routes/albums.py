from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.album import AlbumRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.albums import Album
from app.models.schemas.albums import (
    ListOfAlbumsInResponse,
    AlbumInResponse,
    DEFAULT_ALBUM_LIMIT,
    DEFAULT_ALBUM_OFFSET
)
from app.resources import strings
from app.api.dependencies.album import (
    get_album_by_id_from_path
)


router = APIRouter()

@router.get("", response_model=ListOfAlbumsInResponse, name="albums:get-all")
async def get_all(
    limit: int = Query(DEFAULT_ALBUM_LIMIT, ge=1),
    offset: int = Query(DEFAULT_ALBUM_OFFSET, ge=0),
    album_repo: AlbumRepository = Depends(get_repository(AlbumRepository)),
) -> ListOfAlbumsInResponse:
    albums = await album_repo.get_all(limit=limit, offset=offset)
    return ListOfAlbumsInResponse(albums=albums)

@router.get("/{id}", response_model=AlbumInResponse, name="albums:get-by-id")
async def get_by_id(
    album: Album = Depends(get_album_by_id_from_path),
) -> AlbumInResponse:
    return AlbumInResponse(album=album)

