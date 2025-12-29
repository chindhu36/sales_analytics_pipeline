SELECT
    c.customerid, c.name, c.region
FROM customers c
LEFT JOIN orders o ON c.customerid = o.customerid
WHERE 
    o.orderid IS NULL;