from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Optional, Annotated
from schemas import CategoryRequest
from database import db_dependency
from models import Category

category_router = APIRouter(prefix='/category', tags=['category'])


@category_router.get('/list')
def list(db: db_dependency):
    return db.query(Category).all()

@category_router.post('/store')
def store(request: CategoryRequest, db: db_dependency):
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

@category_router.get('/show/{id}')
def show(id: int, db: db_dependency):
    category = db.query(Category).filter(Category.id == id).first()
    if category is not None:
        return {'message': 'successfull', 'data': category}
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": 'fail'})

@category_router.get('/edit/{id}')
def edit(id: int, db: db_dependency):
    category = db.query(Category).filter(Category.id == id).first()
    if category is not None:
        return {"message": 'edit', 'data': category}
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": 'fail'})

@category_router.put('/update/{id}')
def update(id: int, request: CategoryRequest, db: db_dependency):
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
def delete(id: int, db: db_dependency):
    category = db.query(Category).filter(Category.id == id).first()
    if category is not None:
        db.delete(category)
        db.commit()
        return {'message': 'Category delete'}
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": 'fail'})
