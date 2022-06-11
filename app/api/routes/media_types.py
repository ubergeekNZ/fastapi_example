from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.media_type import MediaTypeRepository
from app.db.errors import EntityDoesNotExist
from app.models.schemas.media_types import (
    ListOfMediaTypesInResponse,
    DEFAULT_MEDIA_LIMIT,
    DEFAULT_MEDIA_OFFSET
    
)
from app.resources import strings

router = APIRouter()

@router.get("", response_model=ListOfMediaTypesInResponse, name="media_types:get-all")
async def get_all(
    limit: int = Query(DEFAULT_MEDIA_LIMIT, ge=1),
    offset: int = Query(DEFAULT_MEDIA_OFFSET, ge=0),
    media_repo: MediaTypeRepository = Depends(get_repository(MediaTypeRepository)),
) -> ListOfMediaTypesInResponse:
    records = await media_repo.get_all(limit=limit, offset=offset)
    print(records)
    return ListOfMediaTypesInResponse(mediaTypes=records)