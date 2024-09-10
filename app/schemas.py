from typing import Optional
from pydantic import BaseModel,EmailStr
from datetime import datetime



# we create more than one model to make the user restricted 
# it could help in make the user can only update one thing in the data
# for ex the user could edit the public option but it can't edit the title 

class PostBase(BaseModel):
    title: str
    content: str
    public: bool =True #its an option pram that user could send it or could send data without it and the deffult will be (true)
    vote: Optional[int] = None


# class CreatePost(BaseModel):
#     title: str
#     contant: str
#     public: bool =True 
#     vote: Optional[int] = None

class PostCreate(PostBase):
    pass 

class Post(PostBase):
    id: int
    created_time:datetime
    class Config:
        from_attributes = True 


class User(BaseModel):
     email: EmailStr
     username: str
     password: str

class UserOut(BaseModel):
    email: EmailStr
    username: str
    created_time:datetime
    class Config:
        from_attributes = True

class UserLogin(BaseModel):

        email:EmailStr
        password:str
        
         