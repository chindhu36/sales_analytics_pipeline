import pandas as pd
from sqlalchemy import create_engine

# Connect to PostgreSQL
engine = create_engine("postgresql+psycopg2://postgres:pswd@localhost/sales_db")

# Load CSV files
customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
orders = pd.read_csv("data/orders.csv")
order_details = pd.read_csv("data/order_details.csv")

# all column names in the csv files to lowercase
customers.columns = customers.columns.str.lower()
products.columns = products.columns.str.lower()
orders.columns = orders.columns.str.lower()
order_details.columns = order_details.columns.str.lower()

# Insert into PostgreSQL
customers.to_sql("customers", engine, if_exists="append", index=False)
products.to_sql("products", engine, if_exists="append", index=False)
orders.to_sql("orders", engine, if_exists="append", index=False)
order_details.to_sql("order_details", engine, if_exists="append", index=False)


print("Data loaded successfully into PostgreSQL!")
