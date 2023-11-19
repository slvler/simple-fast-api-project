from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from schemas import TokenData
from database import db_dependency
from sqlalchemy.orm import Session
from models import User


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e9"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 31

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: int = payload.get("user_id")

        token_data = TokenData(id=id)
    except JWTError:
        return False

    return token_data


def get_current_user(token: str = Depends(oauth2_scheme)):
    return verify_access_token(token)
