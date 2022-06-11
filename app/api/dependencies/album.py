from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.album import AlbumRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.albums import Album
from app.models.schemas.albums import (
    ListOfAlbumsInResponse,
    DEFAULT_ALBUM_LIMIT,
    DEFAULT_ALBUM_OFFSET
)
from app.resources import strings

async def get_album_by_id_from_path(
    id: int,
    album_repo: AlbumRepository = Depends(get_repository(AlbumRepository)),
) -> Album:
    try:
        return await album_repo.get_by_id(id=id)
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.ALBUM_DOES_NOT_EXIST_ERROR,
        )
