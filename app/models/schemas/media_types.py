from typing import List

from app.models.domain.media_types import MediaType
from pydantic import BaseModel

DEFAULT_MEDIA_LIMIT = 20
DEFAULT_MEDIA_OFFSET = 0
class ListOfMediaTypesInResponse(BaseModel):
    mediaTypes: List[MediaType]