from fastapi import APIRouter
from .. import schemas
from ..model import blog_model
from fastapi import Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import blog_repository
from .. import oauth2


router = APIRouter()


@router.post('/blog', tags=['blogs'])
def create(request : schemas.Blog, db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):    
    user = db.query(blog_model.User).filter(blog_model.User.id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id {id} not found')    
    new_blog = blog_model.Blog(title = request.title, body = request.body, user_id= request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 


@router.get('/blog',tags=['blogs'])
def get_all(db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.get_all(db)


@router.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blogs'], response_model=schemas.Blog,)
def get_one(id : int, response = Response,  db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.get_one(id, db)


@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
def delete(id : int, db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(blog_model.Blog).filter(blog_model.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')
    return {'message' : f'deleted blog with id {id}'}

@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED,tags=['blogs'])
def update(id : int, request : schemas.Blog, db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)): 
   blog =  db.query(blog_model.Blog).filter(blog_model.Blog.id == id)
   if not blog.first():
       raise HTTPException (status_code= status.HTTP_404_NOT_FOUND, detail= f'{id} not found')   
   blog.update(request.dict())
   db.commit()
   return 'updated'



