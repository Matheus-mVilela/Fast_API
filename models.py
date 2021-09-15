from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    age: int
    number: int
