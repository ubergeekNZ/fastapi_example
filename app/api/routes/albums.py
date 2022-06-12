from fastapi import APIRouter, Depends, Body, HTTPException, Query, Response
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.album import AlbumRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.albums import Album
from app.models.schemas.albums import (
    ListOfAlbumsInResponse,
    AlbumInResponse,
    AlbumInCreate,
    AlbumInUpdate,
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

@router.get("/{album_id}", response_model=AlbumInResponse, name="albums:get-by-id")
async def get_by_id(
    album: Album = Depends(get_album_by_id_from_path),
) -> AlbumInResponse:
    return AlbumInResponse(album=album)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=AlbumInResponse,
    name="albums:create-album",
)
async def create_album(
    album_create: AlbumInCreate = Body(..., embed=True, alias="album"),
    album_repo: AlbumRepository = Depends(get_repository(AlbumRepository)),
) -> AlbumInResponse:
    album = await album_repo.create_album(album_create.album)
    return AlbumInResponse(album=album)


@router.delete(
    "/{album_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    name="albums:delete-album",
    response_class=Response,
)
async def delete_comment_from_article(
    album: Album = Depends(get_album_by_id_from_path),
    album_repo: AlbumRepository = Depends(get_repository(AlbumRepository)),
) -> None:
    await album_repo.delete(data=album)

@router.put("", response_model=AlbumInResponse, name="albums:update-album")
async def update_album(
    album_update: AlbumInUpdate = Body(..., embed=True, alias="album"),
    album_repo: AlbumRepository = Depends(get_repository(AlbumRepository)),
) -> AlbumInResponse:
    await album_repo.update(data=album_update.album)
    return AlbumInResponse(album=album_update.album)