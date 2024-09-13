# My Project

This project is designed to learn API.

## Starting steps

- create a virtul envroment by using this command 
```cmd 
py -3 -m venv <name>
```
me in this project i used 
```cmd
py -3 -m venv api_env
 ```

- after createing your api requsts run this command to create a server on the localhost ip *loopback ip*
    - there is two ways to create this server 
    1. Fastapi 
        ```cmd 
        fastapi dev <path of the .py file>
        ```
        me in this project i used:
        ``` cmd
        fastapi dev app\main.py
        ```
        - hint it will run only in the local device you can not access this in the local network 
        - To have acces to the server into your local network use this command :
        ``` cmd
        fastapi run app\main.py
        ```
        - To make the server **Reload** with each update in the code 
        ``` cmd
        fastapi run app\main.py --reload
        ```
       - __hint__ : replace `app\main.py` with your main file path
        -------
    2. Uvcorn
        ```cmd
        uvicorn filename:app --reload
        ```
        me in this project i used:
        ```cmd
        uvicorn app.main:app --reload
        ```
        - __hint__ replace `app\main.py` with your main file path
## Libraries in this project
### FastAPI:
To install FastAPI along with all the optional dependencies required for features like databases, web servers, data validation, and asynchronous tasks.
```cmd
pip install fastapi[all]
```

### SQL Alchemy:
SQLAlchemy is a popular SQL toolkit and Object-Relational Mapping (ORM) library for Python that provides a powerful and flexible way to work with databases.

```cmd
pip install SQLAlchemy
```
### Psycopg 2:

``` cmd
pip install psycopg2-binary
```
### Passlib:
Passlib library used for secure password hashing and management.
```cmd 
pip install passlib
```
### bycrpt 
```cmd 
pip install bcrypt
```
### Pyjwt
```cmd 
pip install pyjwt
```

## Description of some code lines

1.  ```python
    app = FastAPI()
    ```
    - __app__ : its a instance of the FastAPI, which is used to create and manage your FastAPI application.
    - __Hint__ : The Root path is `("/")`
---

 2. ``` python 
    @ app.get("/")
    ```
    -  __Decorator__ : start with `@`   
        - app.get(`path`)
    - Each Api function shoud have a Decorator that tell FastAPI that this function sirve that type of HTTP Requests
        - Ex : `@ app.get("/")` -> Tell FastAPI that the next Function will sirve in `get` Request 
    - If the Decorator was in a router file it should have the name of the router 
        - Ex : `@router.get("/sql")`
---

3. ```python 
    router= APIRouter(prefix="/posts",tags=["Posts"])
    ```
    - `APIRouter()`: used to seprate the APIs into files 
        - `prefix`: used to make the decorator more clean by pre define the repeated part in the __path__ of the API    
        - `tags`: used to __group the APIs__ into one group with the defined name into the __documentation__

    - In the `main.py` we have to include the router path 
        - ```python 
            app.include_router(user_api.router)
            ```
            - `user_api.router`: The path of the router
            - `app` : the name of FastAPI instance
---
    
4. ```python 
    def create_post(post: schemas.PostCreate,db:Session = Depends(get_db),username:str = Depends(oauth2.get_cureent_user)):
    ```
    - `Depends`: In this code i used to Call a functions that already created in order to get some data like creating a session with DataBase and check if the user has a Valid Token
        - `db:Session = Depends(get_db)`: Call the function called `get_db` and store the out in variable called `db` with a datatype of `Session`
        db: Session = Depends(get_db):

        - `Depends(get_db)`: Calls the get_db function from the [database](app\database.py) module.
            - __Purpose__: The get_db function is generally used to create and manage a database session (connection) that is passed to your endpoint.
            - `db: Session`: The output of get_db is stored in the variable db and is expected to be of type Session. The Session type typically comes from SQLAlchemy and represents a database connection session.

         - `Depends(oauth2.get_cureent_user)`: Calls the get_cureent_user function from the [oauth2](app\routers\auth.py) module.
            - __Purpose__: This function is used to verify the user’s authentication status, usually by checking if the user has a valid token.
            - `username: str`: The result is stored in the `username` variable, which is expected to be of type `str`. This typically represents the username or user data retrieved from the token.

## App needed in this project
1. [Vs Code](https://code.visualstudio.com/download) : As IDE for coding.
2. [Postman](https://www.postman.com/downloads/) : For doing HTTP Request.
3. [PostgreSQL](https://www.postgresql.org/download/) : For creating Database.


