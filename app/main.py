# use py -3 -m venv <name>  to create a virtual enveroment
# u should also make the cmd or the termenal to use the virtual enveroment 
# run the active.bat in the termenal by enter its path in the termenal 

from fastapi import FastAPI ,Response,status,HTTPException,Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

# pydantic used to make sure the user send data in the format we want 
import psycopg2
from psycopg2.extras import RealDictCursor

from .database import engine,get_db
from . import models,schemas

from sqlalchemy.orm import Session

import time

models.Base.metadata.create_all(bind=engine)



app = FastAPI()



class User(BaseModel):
     username: str
     password: str


# while True:
#      try:
#           conn = psycopg2.connect(host='localhost',database='FastApiDB',user='postgres',password='1100',cursor_factory=RealDictCursor)
#           cursor = conn.cursor()
#           print("connected sucssesfuly")
#           break
#      except Exception as error:
#           print("Error: ",error)
#           time.sleep(2)

## to start the server of Api 
# uvicorn main:app --reload
# if the main file in a package-folder- >> use uvicorn app.main:app --reload
#app.main : app is the file name
# main : the name of the file 
#app : the name of the instance of the fastapi 

# pass opration 

# fast api work by reading line by line if it find the write header it will stop and will not execuate the next header

@ app.get("/")
def root():
    return{"message":"root"}

@app.get("/sql")
def test(db: Session = Depends(get_db)):
     post = db.query(models.Post).all()
     return{'data':post}

@app.get("/posts")  # decorator == start with @   app.get(path)  root path -> "/"
def get_posts(db:Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data":posts}  

@app.get("/posts/{id}")
def get_post(id: int,response:Response,db:Session = Depends(get_db)): # id: int make sure that id could be converted to int value and if not it will send an error code 
     post = db.query(models.Post).filter(models.Post.id == id).first()
     if not post:
          raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                              detail = f"Error id:{id} Not found")
          # response.status_code=status.HTTP_404_NOT_FOUND
          # return{"message":f"Error id:{id} Not found"}
     return{"post details":post}
     
     


#############################################################

#@app.post("/createpost")
#def create_post(payLoad: dict = Body()): 
#    print(payLoad)
#    return{"new post":f"title: {payLoad['title']} || contant: {payLoad['contant']}"}


# the pydantic it has its own schema to convert it to dict use this >> varable_name.dict()
@app.post("/posts",status_code=status.HTTP_201_CREATED)

def create_post(post: schemas.PostCreate,db:Session = Depends(get_db)):
           
          newpost =models.Post(** post.dict())
          db.add(newpost)
          db.commit()
          db.refresh(newpost)
          return{"data":newpost} 

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)

def delete_post(id: int,db:Session = Depends(get_db)):
     del_post = db.query(models.Post).filter(models.Post.id == id)
     if del_post.first() == None:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                              detail=f"Error id:{id} Not found")
     else:
          del_post.delete()
          db.commit()

     return {}
 
@app.put("/posts/{id}")

def update_post(id: int,updated_post:schemas.PostCreate,db:Session = Depends(get_db)):
     querry = db.query(models.Post).filter(models.Post.id == id)
     post = querry.first
     if post == None: #check if the post with id is exist or not 
          # if the post not exist send a code the represent an ERROR
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                              detail=f"Error id:{id} Not found")
     else: 
          querry.update(updated_post.dict())
          db.commit()
     return{"message":querry.first()}




@app.get("/users")
def show_users(db:Session = Depends(get_db)):
    users = db.query(models.User).all()
    return{"data":users}


@app.get("/users/{username}")
def show_user(username:str, db:Session = Depends(get_db)):
     user = db.query(models.User).filter(models.User.username == username).first()
     if not user:
          raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                              detail = f"Error user with username:{username} Not found")    

     return{"data":user} 

@app.post("/users",status_code=status.HTTP_201_CREATED)
def create_user(user:User,db:Session = Depends(get_db)):
     new_user =models.User(** user.dict())
     user = db.query(models.User).filter(models.User.username == new_user.username).first()
     if user :
          raise HTTPException(detail="This user already exist",status_code=status.HTTP_409_CONFLICT)
     else:
          db.add(new_user)
          db.commit()
          db.refresh(new_user)
     return{"data":new_user}