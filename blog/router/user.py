from fastapi import APIRouter
#from .. import schemas, models
from .. import schemas
from ..model import user_model
from fastapi import Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import user_repository


router = APIRouter()


@router.post('/user', response_model=schemas.ShowUser,tags=['users'])
def create_user(request : schemas.User, db : Session = Depends(get_db)):
    return user_repository.create_user(request, db)

@router.get('/user/{id}', response_model=schemas.ShowUser,tags=['users'])
def get_user(id : int, db : Session = Depends(get_db)):
    return user_repository.get_user(id, db)