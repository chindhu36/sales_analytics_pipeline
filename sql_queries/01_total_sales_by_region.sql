SELECT c.region, ROUND(SUM(o.totalamount)) AS total_sales
FROM orders o
JOIN customers c ON c.customerid = o.customerid
GROUP BY c.region
ORDER BY total_sales DESC;

