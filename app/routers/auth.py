from fastapi import APIRouter,Depends,status,HTTPException,Response 
from sqlalchemy.orm import Session

from app import models, schemas,utils,oauth2
from ..database import get_db


router = APIRouter(prefix='/login',tags={'Authentication'})

@router.post('',response_model=schemas.Token)
def Login(user_credentials:schemas.UserLogin,db:Session =Depends(get_db)):

# Check if there is a user with that data 
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
# If not rase an exeption 
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Invalid Credentials')
# Check if the user enter the correct password for that user 
# If not rase an exeption
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Invalid Credentials') 
# Creating the token for the login user   
    access_token =oauth2.create_access_token(data={"username":user.username})

    
    return{'access_token':access_token,'token_type':'bearer'}