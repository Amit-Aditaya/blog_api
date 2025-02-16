


from fastapi import HTTPException, status
from .. import models
from sqlalchemy.orm import Session

def get_all(db : Session):
    return db.query(models.Blog).all()

def get_one(id : int, db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')       
    return blog