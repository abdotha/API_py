from pydantic_settings import BaseSettings
 

# this file used for valided the env variables 
class Settings(BaseSettings):
    DATABASE_USERNAME : str
    DATABASE_PASSWORD : int
    DATABASE_PORT : int
    DATABASE_NAME : str
    DATABASE_HOSTNAME : str
    SECRET_KEY : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int

    class Config:
        env_file = '.env'


settings = Settings()