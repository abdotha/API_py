from passlib.context import CryptContext
pwd_context =  CryptContext(schemes=["bcrypt"],deprecated="auto")


# Hash user input password in order to secure the data 
def hash(password:str):
    hashed_password = pwd_context.hash(password)
    return hashed_password

# compare the attempt pass with user password
def verify(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

if __name__ == "__main__":
    password = '12345'
    hashed_pass = hash(password= password)
    password ='1234'
    print(verify(plain_password= password,hashed_password= hashed_pass))
    
