1. ```cmd
    alembic init alembic 
    ```
    - __Purpose__: create initial enviroment for the `Alembic`

2.  ```cmd
    alembic revision -m "create posts Table"
    ```
    - __Purpose__: create a `Revision file` with a message of `create posts Table`
        - It create a file in under Versions dir there is two functions in this file.
            1. `upgrade`: it will handle in upgrades in our Table. 
            2. `downgrade`: if we want to delete propirty from our Table this will handle that -`Rollback` 
        - Note: `-m "create posts Table"` it's used to add like a label in the file name to make us understatd what this file for 
            - Ex: `-m "create posts Table"` ->File name: b5f09bc69347_create_posts_table.py 
            - `b5f09bc69347`: Revision number
3. ```cmd
    alembic upgrade <Revision_number>
    ```
    - __Purpose__: Used to Call the function upgrade in the Revision file with Revision number = `Revision_number`
        - It help in creating tables or columns in specific table in the DataBase

    - ```cmd 
        alembic upgrade head
        ```
        - __Purpose__: Used to upgrade to the latest Revision 

4. ```cmd
    alembic revision --autogenerate -m "auto"
    ```
    - `--autogenerate`:
        - __Purpose__:Populate revision script with candidate migration operations, based on comparison of database to model - [models.py](app/models.py) -

