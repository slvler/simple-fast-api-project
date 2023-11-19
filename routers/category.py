import time
from fastapi import APIRouter, Depends, HTTPException, status,  Request, Response
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
from typing import Callable

from sqlalchemy.orm import Session
from slugify import slugify

from schemas import CategoryRequest
from schemas import CategoryOut
from database import db_dependency
from models import Category




class TimedRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            before = time.time()
            response: Response = await original_route_handler(request)
            duration = time.time() - before
            response.headers["X-Response-Time"] = str(duration)
            print(f"route duration: {duration}")
            print(f"route response: {response}")
            print(f"route response headers: {response.headers}")
            return response

        return custom_route_handler


category_router = APIRouter(prefix='/category', tags=['category'], route_class=TimedRoute)

@category_router.get('/list')
def list(db: Session = Depends(db_dependency)):
    return db.query(Category).all()

@category_router.post('/store')
def store(request: CategoryRequest, db: Session = Depends(db_dependency)):
    try:
        new_category = Category(
            name=request.name,
            description=request.description,
            is_active=request.is_active,
            slug=request.slug
        )
        db.add(new_category)
        db.commit()
        return {'message': 'successfully'}
    except:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": 'fail'})

@category_router.get('/show/{id}', response_model=CategoryOut)
def show(id: int, db: Session = Depends(db_dependency)):
    category = db.query(Category).filter(Category.id == id).first()
    if category is not None:
        return category
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": 'fail'})

@category_router.get('/edit/{id}')
def edit(id: int, db: Session = Depends(db_dependency)):
    category = db.query(Category).filter(Category.id == id).first()
    if category is not None:
        return {"message": 'edit', 'data': category}
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": 'fail'})

@category_router.put('/update/{id}')
def update(id: int, request: CategoryRequest, db: Session = Depends(db_dependency)):
    category = db.query(Category).filter(Category.id == id).first()
    if category is not None:
        category.name = request.name
        category.description = request.description
        category.is_active = request.is_active
        category.slug = request.slug
        db.commit()
        return {'message': 'update', 'id': id, 'request': request}
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": 'fail'})

@category_router.delete('/delete/{id}')
def delete(id: int, db: Session = Depends(db_dependency)):
    category = db.query(Category).filter(Category.id == id).first()
    if category is not None:
        db.delete(category)
        db.commit()
        return {'message': 'Category delete'}
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": 'fail'})
