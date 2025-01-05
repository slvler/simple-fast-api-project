import time
from typing import Callable

from fastapi import APIRouter, status, Depends, Request, Response
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
from typing import List, Optional, Type
from auth2 import create_access_token
from schemas import AuthRequest
from schemas import RegisterRequest
from models import User
from database import db_dependency
from sqlalchemy.orm import Session



class TimedRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            before = time.time()
            response: Response = await original_route_handler(request)
            auth_token = request.headers.get('Authorization')
            duration = time.time() - before
            response.headers["X-Response-Time"] = str(duration)
            print(f"route duration: {duration}")
            print(f"route response: {response}")
            print(f"route response headers: {response.headers}")
            return response

        return custom_route_handler

auth_router = APIRouter(prefix='/auth',tags=['auth'], route_class=TimedRoute)



@auth_router.get('/login')
async def login(request: AuthRequest, db: Session = Depends(db_dependency)):
     record = db.query(User).filter(User.email == request.email).first()
     if record is not None:
          if record.password == request.password:
               token = create_access_token(data={"user_id": record.id})
               return {'message:': 'successfully', 'token': token}
          else:
              return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": 'fail'})
     else:
          return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": 'fail'})

@auth_router.post('/register')
def register(request: RegisterRequest, db: db_dependency):
     new_user = User(
          name=request.name,
          email=request.email,
          password=request.password
     )
     db.add(new_user)
     db.commit()
     return {"data": request}
