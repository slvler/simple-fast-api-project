from pydantic import BaseModel
from typing import Optional

class BlogRequest(BaseModel):
    name: str
    description: str
    is_active: bool
    slug: str
    category_id: int


class CategoryRequest(BaseModel):
    name: str
    description: str
    is_active: bool
    slug: str

class AuthRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str

class TokenData(BaseModel):
    id: int



class CategoryOut(BaseModel):
    name: str
    description: str
    slug: str

class BlogOut(BaseModel):
    name: str
    description: str
    category_relation: CategoryOut
    class Config:
        orm_mode = True





