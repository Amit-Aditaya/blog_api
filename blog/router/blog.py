from fastapi import APIRouter
from .. import schemas
from ..model import blog_model, user_model
from fastapi import Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import blog_repository
from .. import oauth2



router = APIRouter()


@router.post('/blog', tags=['blogs'])
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.create_blog(request, db)

@router.get('/blog',tags=['blogs'])
def get_all(db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.get_all(db)


@router.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blogs'], response_model=schemas.Blog,)
def get_one(id : int, response = Response,  db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.get_one(id, db)


@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
def delete(id : int, db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.delete_blog(id, db)

@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED,tags=['blogs'])
def update(id : int, request : schemas.Blog, db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)): 
    return blog_repository.edit_blog(id, request, db)



