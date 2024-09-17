# SQL commands

### Notes 
- the SQL specific words could be type in lowercase or uppercase preferred to be uppercase
- each SQL command end with `;`


    ``` sql
    SELECT * FROM products;
    ``` 
    - Return the columns of the database products

- ```*``` => All the columns of the database   
	-   ```sql
         SELECT name FROM products
         ```
        - return the columns with title == `name`  
	- ```SQL 
        SELECT name,id FROM products
        ```
        -  return the columns with title == `name` and `id`
- `products` : name of your database   

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
-------------------
```sql 
SELECT * FROM products WHERE id IN (1,2,3);
```  

- Used to return data which has id = 1 or id = 2 or id = 3
---------

```sql
SELECT * FROM products WHERE name LIKE 'TV%';
SELECT * FROM products WHERE name NOT LIKE 'TV%';
```
- __'TV%'__ : mean to search for any item that its columns `name` start with TV word and any random characters
- __'%TV'__ : mean to search for any item that its columns `name` (end) with 'TV' word 
- __'%TV%'__ : search with `'TV'` `name` in the __Middle__ of the word
- ``NOT LIKE`` : mean to show all the ROW except that have `name` __start__ with 'TV' word and any random characters
------
```sql
SELECT * FROM products ORDER BY price ;
```

- it will order the output depend on the value of the price 
    - __Ascending order: default mode__
- we could use `ASC` for __Ascending__ 
- we could use  `DESSC` for __Descending__ 
- we could order the output by more than one column -> 
    -  ```sql
        SELECT * FROM products ORDER BY  price , time;
        ```
---
```sql
SELECT * FROM products LIMIT 5;
```
- it limit the number of the output
- if we want to skip some ROWS we could use OFFSET -> 
    - ```sql
      SELECT * FROM products LIMIT 5 OFFSET 3;
      ```


# Joining

```sql
SELECT * FROM posts JOIN users ON posts.id = users.id
```
- it will output a new table which  combined the two tables but match the Coloum `id` in the `post` table with `id` in `users` table  