from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.track import TrackRepository
from app.db.errors import EntityDoesNotExist
from app.models.schemas.tracks import (
    ListOfTracksInResponse,
    DEFAULT_TRACKS_LIMIT,
    DEFAULT_TRACKS_OFFSET
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

@router.get("", response_model=ListOfTracksInResponse, name="tracks:get-all")
async def get_all(
    limit: int = Query(DEFAULT_TRACKS_LIMIT, ge=1),
    offset: int = Query(DEFAULT_TRACKS_OFFSET, ge=0),
    track_repo: TrackRepository = Depends(get_repository(TrackRepository)),
) -> ListOfTracksInResponse:
    tracks = await track_repo.get_all()
    return ListOfTracksInResponse(tracks=tracks)

