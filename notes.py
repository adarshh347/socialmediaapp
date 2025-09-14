# if fastapi backend wants to retrieve some data from database through postgres
# the sql query should be something like
# SELECT * FROM products WHERE id =10;
# or  SELECT id,name FROM products WHERE id =10;

# example of shortcut for multiple or operators(using IN)
# SELECT * FROM products WHERE id IN (1,2,3);

# LIKE operator
# SELECT * FROM products WHERE name LIKE 'TV%' or '%e' or'%en%' or NOT LIKE

# LIMIT, OFFSET

# important query : INSERT
# INSERT INTO products(price, name,inventory) VALUES(4,'abc',100)

# returning id: in postgres we are allowed to easily retrieve tuples with specific data through returning id without using select

# prefer serial over int -> because it auto updates

