# use py -3 -m venv <name>  to create a virtual enveroment
# u should also make the cmd or the termenal to use the virtual enveroment 
# run the active.bat in the termenal by enter its path in the termenal 

from fastapi import FastAPI ,Response,status,HTTPException,Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional,List

# pydantic used to make sure the user send data in the format we want 
import psycopg2
from psycopg2.extras import RealDictCursor

from app.routers import auth

from .database import engine,get_db
from . import models,schemas,utils

from sqlalchemy.orm import Session

from .routers import post_api,user_api
from fastapi.middleware.cors import CORSMiddleware

import time


models.Base.metadata.create_all(bind=engine)



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, or specify your domain
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
) 

app.include_router(user_api.router)
app.include_router(post_api.router)
app.include_router(auth.router)

@ app.get("/") 
def root():
    return{"message":"test"}



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