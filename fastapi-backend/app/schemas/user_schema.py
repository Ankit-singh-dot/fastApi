from pydantic import BaseModel
from typing import Optional
class Books(BaseModel):
    id:int
    title:str
    author:str
    publisher:str

class UpdateBookPut(BaseModel):
    title: str
    author: str
    price: float


class UpdateBookPatch(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    price: Optional[float] = None