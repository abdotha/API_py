import time
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Sessionlocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()


def connect_database():
    while True:
     try:
          conn = psycopg2.connect(host='localhost',database='FastApiDB',user='postgres',password='1100',cursor_factory=RealDictCursor)
          cursor = conn.cursor()
          print("connected sucssesfuly")
          break
     except Exception as error:
          print("Error: ",error)
          time.sleep(2)
          