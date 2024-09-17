from .. import schemas,models,utils
from fastapi import status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List

# tags help in dec of the Api 
# prefix = "/users"  -> it make the decorator more clean 
# the decorator was like this 
# @router.get("/users",response_model=List[schemas.UserOut])

router= APIRouter(prefix="/users",tags=["Users"])



@router.get("",response_model=List[schemas.UserOut])
def show_users(db:Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@router.post("",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user:schemas.User,db:Session = Depends(get_db)):
# We need to hash the password the the user input for its account
     hashed_password= utils.hash(user.password)
     user.password = hashed_password
     new_user =models.User(** user.dict())
     user = db.query(models.User).filter(models.User.username == new_user.username).first()
     if user :
          raise HTTPException(detail="This user already exist",status_code=status.HTTP_409_CONFLICT)
     else:
          db.add(new_user)
          db.commit()
          db.refresh(new_user)
          return new_user
     
@router.get("/{username}",response_model=schemas.UserOut)
def show_user(username:str, db:Session = Depends(get_db)):
     user = db.query(models.User).filter(models.User.username == username).first()
     if not user:
          raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                              detail = f"Error user with username:{username} Not found")    

     return user 
     

