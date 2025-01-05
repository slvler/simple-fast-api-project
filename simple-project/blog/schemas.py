from pydantic import BaseModel

class storeClass(BaseModel):
    title: str
    content: str
    vote: int
    status: bool

class updateClass(BaseModel):
    title: str
    content: str
    vote: int
    status: bool