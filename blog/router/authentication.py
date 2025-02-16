from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schemas, database
from ..model import user_model as models
from ..schemas import Token
from ..token import create_access_token

router = APIRouter(tags=['authentication'])


@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid credentials')
    
    if user.password != request.password:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid password')

  
    access_token = create_access_token(
        data={"sub": user.email},
    )

    return Token(access_token=access_token, token_type="bearer")