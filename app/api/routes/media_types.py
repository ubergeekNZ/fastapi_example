from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.media_type import MediaTypeRepository
from app.db.errors import EntityDoesNotExist
from app.models.schemas.media_types import (
    ListOfMediaTypesInResponse
)
from app.resources import strings

router = APIRouter()

# @router.get(
#     "",
#     response_model=ListOfCommentsInResponse,
#     name="comments:get-comments-for-article",
# )
# @router.get("/", status_code=200) 
# async def root():
#     return {"message": "Hello World"}

@router.get("", response_model=ListOfMediaTypesInResponse, name="media_types:get-all")
async def get_all(
    media_repo: MediaTypeRepository = Depends(get_repository(MediaTypeRepository)),
) -> ListOfMediaTypesInResponse:
    records = await media_repo.get_all()
    print(records)
    return ListOfMediaTypesInResponse(mediaTypes=records)