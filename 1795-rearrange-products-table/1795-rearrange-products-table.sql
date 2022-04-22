SELECT * FROM (SELECT product_id AS product_id, 
'store1' AS store, 
store1 AS price
FROM Products
    UNION
SELECT product_id, 
'store2', 
store2
FROM Products
    UNION
SELECT product_id, 
'store3', 
store3
FROM Products) as Prices
WHERE price IS NOT NULL