from sqlalchemy import TIMESTAMP, Column, Integer,String,Boolean,text
from .database import Base


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    contant = Column(String,nullable=False)
    public = Column(Boolean,nullable=False,server_default='True')
    created_time = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()')) 
    vote = Column(Integer,server_default='0')