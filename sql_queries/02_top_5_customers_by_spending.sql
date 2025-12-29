SELECT
    c.name AS customer_name,
    ROUND(SUM(o.totalamount), 2) AS total_spent
FROM orders o
INNER JOIN
    customers c ON c.customerid = o.customerid
GROUP BY 
    c.name
ORDER BY 
    total_spent DESC
LIMIT 5;