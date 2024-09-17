

from fastapi import APIRouter,status,Depends,HTTPException

from app import models, oauth2, schemas
from app.database import get_db
from sqlalchemy.orm import Session


router= APIRouter(prefix="/vote",tags=["Vote"])

@router.post("",status_code=status.HTTP_201_CREATED)
def voting(vote:schemas.Vote,db:Session = Depends(get_db),username:str = Depends(oauth2.get_cureent_user)):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"This post dose not exits")
    
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,models.Vote.username == username.username)
    found_vote = vote_query.first()
    if(vote.vote == True):
        # print(found_vote.username)
        # print(found_vote.post_id)

        if found_vote:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f'user {username.username} has already voted in this post')
        else:
            new_vote = models.Vote(post_id =vote.post_id,username = username.username)
            db.add(new_vote)
            db.commit()
            return{"message":"successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user {username.username} dose not vote in this post')
        else:
            vote_query.delete()
            db.commit()
            return{"message":"successfully deleted vote"}
 