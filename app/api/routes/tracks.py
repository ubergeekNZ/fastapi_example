from fastapi import APIRouter, Depends, HTTPException, Query, Response, Body
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.track import TrackRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.tracks import Track
from app.models.schemas.tracks import (
    ListOfTracksInResponse,
    TrackInCreate,
    TrackInResponse,
    TrackInUpdate,
    DEFAULT_TRACKS_LIMIT,
    DEFAULT_TRACKS_OFFSET
)
from app.resources import strings
from app.api.dependencies.track import (
    get_track_by_id_from_path
)

router = APIRouter()

@router.get("", response_model=ListOfTracksInResponse, name="tracks:get-all")
async def get_all(
    limit: int = Query(DEFAULT_TRACKS_LIMIT, ge=1),
    offset: int = Query(DEFAULT_TRACKS_OFFSET, ge=0),
    track_repo: TrackRepository = Depends(get_repository(TrackRepository)),
) -> ListOfTracksInResponse:
    tracks = await track_repo.get_all(limit=limit, offset=offset)
    return ListOfTracksInResponse(tracks=tracks)


@router.get("/{track_id}", response_model=TrackInResponse, name="tracks:get-by-id")
async def get_by_id(
    track: Track = Depends(get_track_by_id_from_path),
) -> TrackInResponse:
    return TrackInResponse(track=track)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=TrackInResponse,
    name="tracks:create-track",
)
async def create_track(
    track_create: TrackInCreate = Body(..., embed=True, alias="track"),
    track_repo: TrackRepository = Depends(get_repository(TrackRepository)),
) -> TrackInResponse:
    track = await track_repo.create_track(track_create.track)
    return TrackInResponse(track=track)


@router.delete(
    "/{track_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    name="tracks:delete-track",
    response_class=Response,
)
async def delete_comment_from_article(
    track: Track = Depends(get_track_by_id_from_path),
    track_repo: TrackRepository = Depends(get_repository(TrackRepository)),
) -> None:
    await track_repo.delete(data=track)

@router.put("", response_model=TrackInResponse, name="tracks:update-track")
async def update_track(
    track_update: TrackInUpdate = Body(..., embed=True, alias="track"),
    track_repo: TrackRepository = Depends(get_repository(TrackRepository)),
) -> TrackInResponse:
    await track_repo.update(data=track_update.track)
    return TrackInResponse(track=track_update.track)