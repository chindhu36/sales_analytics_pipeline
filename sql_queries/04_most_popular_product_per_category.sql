SELECT DISTINCT ON (p.category)
    p.category,
    p.name AS product_name,
    p.price AS price
FROM products p
ORDER BY p.category, p.price DESC;
