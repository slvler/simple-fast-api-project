from pydantic import BaseModel


class loginRequest(BaseModel):
    email: str
    password: str

class registerRequest(BaseModel):
    name: str
    email: str
    password: str
    re_password: str

