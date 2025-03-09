

from .. import schemas
from ..model import user_model
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

def create_user(request : schemas.User, db : Session):
    new_user = user_model.User(name = request.name, email = request.email, password = request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id : int, db : Session):
    user = db.query(user_model.User).filter(user_model.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id {id} not found')
    return user