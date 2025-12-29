import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:pswd@localhost/sales_db")

#  monthly sales
with open('sql_queries/03_monthly_sales_trend.sql', 'r') as file:
    query = file.read()

df = pd.read_sql(query, engine)

print(df)

df.plot(kind="bar", x="month", y="monthly_sales", legend=False, title="Total Sales by month")
plt.ylabel("monthly_sales")
plt.show()

# Save the figure
plt.savefig("plots/monthly_sales.png", dpi=300, bbox_inches="tight")

# Also display it (optional)
plt.show()


# Total sales by region
with open('sql_queries/01_total_sales_by_region.sql', 'r') as file:
    query = file.read()

df = pd.read_sql(query, engine)

print(df)

df.plot(kind="bar", x="region", y="total_sales", legend=False, title="Total Sales by Region")
plt.ylabel("Sales")
plt.show()

# Save the figure
plt.savefig("plots/sales_by_region.png", dpi=300, bbox_inches="tight")

# Also display it (optional)
#plt.show()

