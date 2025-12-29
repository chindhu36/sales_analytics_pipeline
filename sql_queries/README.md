# 📂 SQL Queries Overview

SQL queries for analyzing sales data in the Sales Analytics Pipeline project.Here the use-case uses PostgreSQL.

---

### 🧾 Query Descriptions

| Filename                                 | Description |
|------------------------------------------|-------------|
| `01_total_sales_by_region.sql`           | Calculates total sales per region. Useful for regional performance analysis. |
| `02_top_5_customers_by_spending.sql`     | Identifies the top 5 customers with the highest total spend. |
| `03_monthly_sales_trend.sql`             | Aggregates total sales per month to reveal trends over time. |
| `04_most_popular_product_per_category.sql` | Selects the most expensive (popular) product per category using `DISTINCT ON`. |
| `05_customers_without_orders.sql`        | Lists customers who haven't placed any orders (anti-join logic). |

---

💡 **Note:** All queries assume the relational schema defined in [`sql/schema.sql`](../sql/schema.sql)
