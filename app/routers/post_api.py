from .. import schemas,models,utils
from fastapi import FastAPI ,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List  



router= APIRouter()

@router.get("/sql")
def test(db: Session = Depends(get_db)):
     post = db.query(models.Post).all()
     return{'data':post}

@router.get("/posts",response_model=List[schemas.Post])  # decorator == start with @   router.get(path)  root path -> "/"
async def get_posts(db:Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts 

@router.get("/posts/{id}",response_model=schemas.Post)
def get_post(id: int,response:Response,db:Session = Depends(get_db)): # id: int make sure that id could be converted to int value and if not it will send an error code 
     post = db.query(models.Post).filter(models.Post.id == id).first()
     if not post:
          raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                              detail = f"Error id:{id} Not found")
          # response.status_code=status.HTTP_404_NOT_FOUND
          # return{"message":f"Error id:{id} Not found"}
     return post
     
     


#############################################################

#@router.post("/createpost")
#def create_post(payLoad: dict = Body()): 
#    print(payLoad)
#    return{"new post":f"title: {payLoad['title']} || contant: {payLoad['contant']}"}


# the pydantic it has its own schema to convert it to dict use this >> varable_name.dict()
@router.post("/posts",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
# response_model=schemas.Post >> it filter and orgnize the output
# note the return must be a dict only or list of dicts not like this --> return {data:newpost} it will cause an ERROR 
async def create_post(post: schemas.PostCreate,db:Session = Depends(get_db)):
           
          newpost =models.Post(** post.dict())
          db.add(newpost)
          db.commit()
          db.refresh(newpost)
          return newpost

@router.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)

def delete_post(id: int,db:Session = Depends(get_db)):
     del_post = db.query(models.Post).filter(models.Post.id == id)
     if del_post.first() == None:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                              detail=f"Error id:{id} Not found")
     else:
          del_post.delete()
          db.commit()

     return {}
 
@router.put("/posts/{id}")

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
