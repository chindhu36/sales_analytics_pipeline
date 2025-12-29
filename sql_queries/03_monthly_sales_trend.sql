SELECT 
    DATE_TRUNC('month', orderdate::date) AS month,
    ROUND(SUM(totalamount)::numeric, 2) AS monthly_sales
FROM 
    orders
GROUP BY 
    month
ORDER BY 
    month;