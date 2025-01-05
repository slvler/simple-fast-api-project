from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from auth2 import get_current_user
from database import db_dependency
from fastapi.responses import JSONResponse
from models import Category
from schemas import TokenData
from models import User

profile_router = APIRouter(prefix='/profile', tags=['profile'])


@profile_router.get('/account')
def all(db: Session = Depends(db_dependency), user_id: TokenData = Depends(get_current_user)):
    return db.query(User).filter(User.id == user_id.id).first()