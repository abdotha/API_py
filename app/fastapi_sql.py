# use py -3 -m venv <name>  to create a virtual enveroment
# u should also make the cmd or the termenal to use the virtual enveroment 
# run the active.bat in the termenal by enter its path in the termenal 

from fastapi import FastAPI ,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
# pydantic used to make sure the user send data in the format we want 
import psycopg2
from psycopg2.extras import RealDictCursor

import time

app = FastAPI()

class Post(BaseModel):
    title: str
    contant: str
    public: bool =True #its an option pram that user could send it or could send data without it and the deffult will be (true)
    vote: Optional[int] = None

while True:
     try:
          conn = psycopg2.connect(host='localhost',database='FastApiDB',user='postgres',password='1100',cursor_factory=RealDictCursor)
          cursor = conn.cursor()
          print("connected sucssesfuly")
          break
     except Exception as error:
          print("Error: ",error)
          time.sleep(2)
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

@app.get("/posts")  # decorator == start with @   app.get(path)  root path -> "/"
def get_posts():
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    return {"data":posts}  

@app.get("/posts/{id}")
def get_post(id: int,response:Response): # id: int make sure that id could be converted to int value and if not it will send an error code 
     cursor.execute("""SELECT * FROM posts WHERE id = %s """,(str(id)))
     post =cursor.fetchone()
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

def create_post(post: Post): 
          cursor.execute("""INSERT INTO posts (title, contant, public) VALUES (%s, %s, %s) RETURNING * """,(post.title,post.contant,post.public))
          newpost =cursor.fetchone()
          conn.commit()
          return{"data":newpost} 

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)

def delete_post(id: int):
     cursor.execute("DELETE FROM posts WHERE id  = %s RETURNING * ",(str(id)))
     del_post=cursor.fetchone()
     conn.commit()
     if del_post == None:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                              detail=f"Error id:{id} Not found")
     return {}
 
@app.put("/posts/{id}")

def update_post(id: int,post:Post):

     cursor.execute("UPDATE posts SET title = %s, contant = %s,public = %s  WHERE  id = %s RETURNING * ",(post.title,post.contant,post.public,str(id)))
     post_updated=cursor.fetchone()
     conn.commit()
     if post_updated == None: #check if the post with id is exist or not 
          # if the post not exist send a code the represent an ERROR
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                              detail=f"Error id:{id} Not found")
     return{"message":post_updated}