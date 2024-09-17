from sqlalchemy import func
from .. import schemas,models,oauth2
from fastapi import Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List, Optional  


#router used to seprate the APIs into files

# prefix used to pre define the repeated part in the path 
# ex all the pathes start with /posts 
# tags group all the apis in this router into the same group in the documentation 

router= APIRouter(prefix="/posts",tags=["Posts"])




#     posts = db.query(models.Post).filter(models.Post.title.contains(search))

# decorator == start with @   router.get(path)  root path -> "/"                ,response_model=List[schemas.Post]
@router.get("",response_model=List[schemas.PostOut])  
async def get_posts(db:Session = Depends(get_db),search:Optional[str]=''):

    posts = db .query(models.Post,func.count(models.Vote.post_id).label("vote")).join(models.Vote,models.Vote.post_id == models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).all()
    return posts
# @router.get("/{user_username}",response_model=List[schemas.Post],)  
# async def get_posts(user_username:str,db:Session = Depends(get_db),username:str = Depends(oauth2.get_cureent_user)):
    
#     posts = db.query(models.Post).filter(models.Post.username == user_username).all()
#     return posts 

@router.get("/{id}",response_model=schemas.PostOut)
# id: int make sure that id could be converted to int value and if not it will send an error code 
def get_post(id: int,response:Response,db:Session = Depends(get_db),username:str = Depends(oauth2.get_cureent_user)): 
     
     post = db.query(models.Post).filter(models.Post.id == id).first()
     if not post:
          raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                              detail = f"Error id:{id} Not found")
     else:
          if post.username != username.username:
               raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
          post = db.query(models.Post,func.count(models.Vote.post_id).label("vote")).join(models.Vote,models.Vote.post_id == models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
          # response.status_code=status.HTTP_404_NOT_FOUND
          # return{"message":f"Error id:{id} Not found"}
     return post
     
     

#@router.post("/createpost")
#def create_post(payLoad: dict = Body()): 
#    print(payLoad)
#    return{"new post":f"title: {payLoad['title']} || contant: {payLoad['contant']}"}


# the pydantic it has its own schema to convert it to dict use this >> varable_name.dict()
@router.post("",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
# response_model=schemas.Post >> it filter and orgnize the output
# note the return must be a dict only or list of dicts not like this --> return {data:newpost} it will cause an ERROR 
# username:str = Depends(oauth2.get_cureent_user) => used for calling a function that check if the user pass a valid token and return the username of this user
async def create_post(post: schemas.PostCreate,db:Session = Depends(get_db),username:str = Depends(oauth2.get_cureent_user)):
          
          print(username)
          newpost =models.Post(username=username.username,** post.model_dump())
          db.add(newpost)
          db.commit()
          db.refresh(newpost)
          # newpost.username=username.username
          return newpost 

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)

def delete_post(id: int,db:Session = Depends(get_db),username:str = Depends(oauth2.get_cureent_user)):
     post_query = db.query(models.Post).filter(models.Post.id == id)

     del_post =post_query.first()

     if del_post == None:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                              detail=f"Error id:{id} Not found")
     else:
          if del_post.username != username.username:
               raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
          
          post_query.delete()
          db.commit()

     return {}
 
@router.put("/{id}")

def update_post(id: int,updated_post:schemas.PostCreate,db:Session = Depends(get_db),username:str = Depends(oauth2.get_cureent_user)):
     querry = db.query(models.Post).filter(models.Post.id == id)
     post = querry.first()
#check if the post with id is exist or not
     if post == None:  
# if the post not exist send a code the represent an ERROR
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                              detail=f"Error id:{id} Not found")
     else:
          if post.username != username.username:
               raise HTTPException(status_code=status.HTTP_403_FORBIDDEN) 
          
          querry.update(updated_post.model_dump())
          db.commit()
     return{"message":querry.first()}
