from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.media_type import MediaTypeRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.media_types import MediaType
from app.resources import strings

async def get_mediaType_by_id_from_path(
    media_type_id: int,
    mediaType_repo: MediaTypeRepository = Depends(get_repository(MediaTypeRepository)),
) -> MediaType:
    try:
        return await mediaType_repo.get_by_id(id=media_type_id)
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.MEDIA_DOES_NOT_EXIST_ERROR,
        )
