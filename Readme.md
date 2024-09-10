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

## Description of some code lines

1.  ```python
    app = FastAPI()
    ```
    - __app__ : its a instance of the FastAPI, which is used to create and manage your FastAPI application.
    - __Hint__ : The Root path is `("/")`
-------------------

 2. ``` python 
    @ app.get("/")
    ```
    -  __Decorator__ : start with `@`   
        - app.get(`path`)
    - Each Api function shoud have a Decorator that tell FastAPI that this function sirve that type of HTTP Requests
        - Ex : `@ app.get("/")` -> Tell FastAPI that the next Function will sirve in `get` Request 
----------------------
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


## App needed in this project
1. [Vs Code](https://code.visualstudio.com/download) : As IDE for coding.
2. [Postman](https://www.postman.com/downloads/) : For doing HTTP Request.
3. [PostgreSQL](https://www.postgresql.org/download/) : For creating Database.


