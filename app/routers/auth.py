from fastapi import APIRouter,Depends,status,HTTPException,Response 
from sqlalchemy.orm import Session

from app import models, schemas,utils,oauth2
from ..database import get_db


router = APIRouter(prefix='/Login',tags={'Authentication'})

@router.post('')
def Login(user_credentials:schemas.UserLogin,db:Session =Depends(get_db)):

# Check if there is a user with that data 
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
# if not rase an exeption 
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Invalid Credentials')
# Check if the user enter the correct password for that user 
# if not rase an exeption
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Invalid Credentials') 
    
    access_token =oauth2.create_access_token(data={"username":user.username})

    
    return{'access Token':access_token,'token_type':'bearer'}