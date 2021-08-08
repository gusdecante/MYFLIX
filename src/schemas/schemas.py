from pydantic import BaseModel
from typing import Optional

class Serie(BaseModel):
  id: Optional[int] = None
  title: str
  year: int
  gender: str
  qtt_seasons: int
  
  class Config:
    orm_mode: True