from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer,String,Boolean,text
from .database import Base

# Note with any edit in the model we have to delete the table manually 
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    public = Column(Boolean,nullable=False,server_default='True')
    created_time = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()')) 
    # vote = Column(Integer,server_default='0')
    username =Column(String,ForeignKey("users.username",ondelete="CASCADE"),nullable=False)

class User(Base):
    __tablename__ = "users"
    email = Column(String,unique=True,nullable=False)
    username = Column(String,primary_key=True,nullable=False)
    password = Column(String,nullable=False)
    created_time = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()')) 

class Vote(Base):
    __tablename__='vote'
    username =Column(String,ForeignKey("users.username",ondelete="CASCADE"),nullable=False,primary_key=True)
    post_id = Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),nullable=False,primary_key=True)
    
