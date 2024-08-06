from typing import Optional
from pydantic import BaseModel



# we create more than one model to make the user restricted 
# it could help in make the user can only update one thing in the data
# for ex the user could edit the public option but it can't edit the title 

class PostBase(BaseModel):
    title: str
    contant: str
    public: bool =True #its an option pram that user could send it or could send data without it and the deffult will be (true)
    vote: Optional[int] = None


# class CreatePost(BaseModel):
#     title: str
#     contant: str
#     public: bool =True #its an option pram that user could send it or could send data without it and the deffult will be (true)
#     vote: Optional[int] = None

class PostCreate(PostBase):
    pass 


         