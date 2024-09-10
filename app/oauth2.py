from jose import JWTError
from datetime import datetime,timedelta
import jwt

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data:dict):
    to_encode = data.copy()
    # add the expiration time of the token = [The time of creation + ACCESS_TOKEN_EXPIRE_MINUTES] 
    expire = datetime.now()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # add this part to the data[copy] = to_encode
    to_encode.update({"exp":expire})
    
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encoded_jwt 
