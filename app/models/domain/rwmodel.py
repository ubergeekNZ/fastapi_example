import datetime

from pydantic import BaseConfig, BaseModel

class RWModel(BaseModel):
    class Config:
        orm_mode = True