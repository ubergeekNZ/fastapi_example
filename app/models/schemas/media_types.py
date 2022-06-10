from typing import List

from app.models.domain.media_types import MediaType
from pydantic import BaseModel


class ListOfMediaTypesInResponse(BaseModel):
    mediaTypes: List[MediaType]