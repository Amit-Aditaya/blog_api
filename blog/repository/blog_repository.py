


from fastapi import HTTPException, status, Depends
from .. import schemas
from ..model import user_model, blog_model
#from .. import models
from ..model import blog_model as models
from sqlalchemy.orm import Session
from ..database import get_db

def get_all(db : Session):
    return db.query(models.Blog).all()

def get_one(id : int, db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')       
    return blog


def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id {request.user_id} not found')
    new_blog = blog_model.Blog(title=request.title, body=request.body, user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete_blog(id : int, db : Session = Depends(get_db)):
    blog = db.query(blog_model.Blog).filter(blog_model.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')
    return {'message' : f'deleted blog with id {id}'}

def edit_blog(id : int, request : schemas.Blog, db : Session = Depends(get_db)):
    blog = db.query(blog_model.Blog).filter(blog_model.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')
    blog.title = request.title
    blog.body = request.body
    db.commit()
    return blog