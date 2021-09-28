from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    age: int
    fone: int

    class Config:
        orm_mode = True