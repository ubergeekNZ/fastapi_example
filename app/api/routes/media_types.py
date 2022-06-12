from fastapi import APIRouter, Depends, HTTPException, Query, Response, Body
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.media_type import MediaTypeRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.media_types import MediaType
from app.models.schemas.media_types import (
    ListOfMediaTypesInResponse,
    MediaTypeInResponse,
    MediaTypeInCreate,
    MediaTypeInUpdate,
    DEFAULT_MEDIA_LIMIT,
    DEFAULT_MEDIA_OFFSET
)
from app.resources import strings
from app.api.dependencies.media_type import (
    get_mediaType_by_id_from_path
)

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


@router.get("/{mediatype_id}", response_model=MediaTypeInResponse, name="mediatypes:get-by-id")
async def get_by_id(
    mediatype: MediaType = Depends(get_mediaType_by_id_from_path),
) -> MediaTypeInResponse:
    return MediaTypeInResponse(mediatype=mediatype)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=MediaTypeInResponse,
    name="mediatypes:create-mediatype",
)
async def create_mediatype(
    mediatype_create: MediaTypeInCreate = Body(..., embed=True, alias="mediatype"),
    mediatype_repo: MediaTypeRepository = Depends(get_repository(MediaTypeRepository)),
) -> MediaTypeInResponse:
    mediatype = await mediatype_repo.create_mediatype(mediatype_create.mediatype)
    return MediaTypeInResponse(mediatype=mediatype)


@router.delete(
    "/{mediatype_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    name="mediatypes:delete-mediatype",
    response_class=Response,
)
async def delete_comment_from_article(
    mediatype: MediaType = Depends(get_mediaType_by_id_from_path),
    mediatype_repo: MediaTypeRepository = Depends(get_repository(MediaTypeRepository)),
) -> None:
    await mediatype_repo.delete(data=mediatype)

@router.put("", response_model=MediaTypeInResponse, name="mediatypes:update-mediatype")
async def update_mediatype(
    mediatype_update: MediaTypeInUpdate = Body(..., embed=True, alias="mediatype"),
    mediatype_repo: MediaTypeRepository = Depends(get_repository(MediaTypeRepository)),
) -> MediaTypeInResponse:
    await mediatype_repo.update(data=mediatype_update.mediatype)
    return MediaTypeInResponse(mediatype=mediatype_update.mediatype)