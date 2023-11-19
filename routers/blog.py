from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from slugify import slugify

from schemas import BlogRequest
from models import Blog
from database import db_dependency

blog_router = APIRouter(prefix='/blog', tags=['blog'])


@blog_router.get('/list')
def list(db: Session = Depends(db_dependency)):
    return db.query(Blog).all()


@blog_router.post('/store')
def store(request: BlogRequest, db: Session = Depends(db_dependency)):
    try:
        new_blog = Blog(
            name=request.name,
            description=request.description,
            is_active=request.is_active,
            slug=slugify(request.name),
            category_id=request.category_id
        )
        db.add(new_blog)
        db.commit()
        return {'message': 'successfully'}
    except:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": 'fail'})


@blog_router.get('/show/{blog_id}')
def show(blog_id: int, db: Session = Depends(db_dependency)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if blog is not None:
        return {'message': 'successfully', 'blog': blog}
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": 'fail'})


@blog_router.get('/edit/{id}')
def edit(id: int, db: Session = Depends(db_dependency)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if blog is not None:
        return {"message": 'edit', 'data': blog}
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": 'fail'})


@blog_router.put('/update/{blog_id}')
def update(blog_id: int, request: BlogRequest, db: Session = Depends(db_dependency)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if blog is not None:
        blog.name = request.name
        blog.description = request.description
        blog.is_active = request.is_active
        blog.category_id = request.category_id
        blog.slug = slugify(request.name)
        db.commit()
        return {'message': 'successfully'}
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": 'fail'})


@blog_router.delete('/delete/{blog_id}')
def delete(blog_id: int, db: Session = Depends(db_dependency)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if blog is not None:
        db.delete(blog)
        db.commit()
        return {'message': 'Blog delete'}
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": 'fail'})
