from fastapi import APIRouter
from .. import schemas, models
from fastapi import Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter()


@router.post('/user', response_model=schemas.ShowUser,tags=['users'])
def create_user(request : schemas.User, db : Session = Depends(get_db)):
    new_user = models.User(name = request.name, email = request.email, password = request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/user/{id}', response_model=schemas.ShowUser,tags=['users'])
def get_user(id : int, db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')
    return user