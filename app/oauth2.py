from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime,timedelta
import jwt

from app import schemas
from .config import settings

 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES


def create_access_token(data:dict):
    to_encode = data.copy()
# Add the expiration time of the token = [The time of creation + ACCESS_TOKEN_EXPIRE_MINUTES] 
    expire = datetime.utcnow()+ timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
# Add this part to the data[copy] = to_encode
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encoded_jwt 

def verify_access_token(token:str,credentials_exeption):
    try:
# Decode the token to check if it real a valid Token or not
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str = payload.get("username")
        if username is None:
            raise credentials_exeption
 
        token_data = schemas.TokenData(username = username)
    except:
        raise credentials_exeption
    return token_data


def get_cureent_user(token:str =Depends(oauth2_scheme)):
    credentials_exeption =HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid Credentials',
                                        headers={"WWW-Authenticate": "Bearer"})
    return verify_access_token(token=token,credentials_exeption=credentials_exeption)