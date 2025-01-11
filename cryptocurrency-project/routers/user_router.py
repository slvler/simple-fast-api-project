from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from schemas.user_shemas import loginRequest, registerRequest
from models.models import User
from config.database import SessionLocal
from sqlalchemy.orm import Session

user_router = APIRouter(prefix='/users', tags=['users'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@user_router.post("/register")
def register(request: registerRequest, db: Session = Depends(get_db)):
    new_user = User(name=request.name, email=request.email, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

    content = {"message": "Success", "data": new_user}
    return JSONResponse(content=content, status_code=200)

@user_router.post("/login")
def login(request: loginRequest):
    content = {"message": "Custom response example"}
    return JSONResponse(content=content, status_code=200)