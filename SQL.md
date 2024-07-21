# SQL commands

### Notes 
- the SQL specific words could be type in lowercase or uppercase preferred to be uppercase
- each SQL command end with `;`


 ``` sql
SELECT * FROM products;
``` 
>  return the columns of the database products

- ```*``` => All the columns of the database   
	-   ```sql
         SELECT name FROM products
         ```
        > return the columns with title == `name`  
	- ```SQL 
        SELECT name,id FROM products
        ```
        > return the columns with title == `name` and `id`
- `products` => name of your database   

---------------------
```SQL
SELECT id AS products_id FROM products;	
```
- Change the name of the `id` column to`products_id` in database called `products`
--------------
```SQL
SELECT * FROM products WHERE id = 10 ;
```
- Return the Row with its `id` column = `10` from database with name `products`

- If the column we want to search in is a (text) or (varying char) => use __'data'__ single quotes   
	-  EX:      
    ```SQL
    SELECT * FROM products WHERE name = 'TV';
     ```
- we could replace `=` with `<` , `>` , `<=` or `>=`  
	-  EX: 
    ```SQL
    SELECT * FROM products WHERE id >= 10 ;
    ```
- we could use __Not equal__ by using `!=` or `<>` 	
	-  EX: 
    ``` SQL
    SELECT * FROM products WHERE id != 5;
    ```
- we could use `or` , `and` to see if in row has specific values
	- Ex: To see the items that have `name` equal with  __TV__ and `price` equal __100__ 

        ``` SQL  
        SELECT * FROM products WHERE name = 'TV' AND price = 100 ;
        ```
	- Ex: To see the items that have `price` equal to __100__ or equal 
    to __200__
     
        ``` SQL
		SELECT * FROM products WHERE price = 100 or price = 200 ; 
        ```