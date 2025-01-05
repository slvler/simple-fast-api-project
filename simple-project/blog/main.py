from fastapi import FastAPI, Depends, status, HTTPException
#from .schemas import storeClass, updateClass
#from . import models
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session


models.Base.metadata.create_all(engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/blog")
def index(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.post("/blog", status_code=status.HTTP_201_CREATED)
def store(request: schemas.storeClass, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, content=request.content, vote=request.vote, status=request.status)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog/{id}")
def show(id: int, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        return {"message": "not found"}
    return blogs


@app.put("/blog/{id}")
def update(id: int, request: schemas.updateClass, db: Session = Depends(get_db)):


    blog = db.query(models.Blog).filter(models.Blog.id == id)


    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'{id} id not found')

    update_data = request.dict(exclude_unset=True)
    if "title" in update_data:
        blog.update({"title": update_data["title"]})
    if "content" in update_data:
        blog.update({"content": update_data["content"]})


    # blog.update(request)
    db.commit()
    return {"message": "success"}

@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {"message": "success"}