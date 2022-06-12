from typing import List, Optional

from app.models.domain.media_types import MediaType
from app.models.schemas.rwschema import RWSchema
from pydantic import BaseModel


DEFAULT_MEDIA_LIMIT = 20
DEFAULT_MEDIA_OFFSET = 0
class ListOfMediaTypesInResponse(BaseModel):
    mediaTypes: List[MediaType]

class MediaTypeInResponse(RWSchema):
    mediatype: MediaType


class MediaTypeInCreate(RWSchema):
    mediatype: MediaType

class MediaTypeInUpdate(BaseModel):
    mediatype_id: Optional[int]=None
    name: Optional[str] = None