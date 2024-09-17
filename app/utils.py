from passlib.context import CryptContext
pwd_context =  CryptContext(schemes=["bcrypt"],deprecated="auto")


# Hash user input password in order to secure the data 
def hash(password:str):
    hashed_password = pwd_context.hash(password)
    return hashed_password

# compare the attempt pass with user password
def verify(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)
