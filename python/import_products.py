import pandas as pd
import mysql.connector

# Read CSV
df = pd.read_csv("data/products.csv")

# Connect MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="retail_sales_db"
)

cursor = connection.cursor()

print("✅ Products CSV Read Successfully")
print("✅ MySQL Connected Successfully")

# Insert Data
for index, row in df.iterrows():

    cursor.execute(
        """
        INSERT INTO products
        (product_name, category, brand, price, stock_quantity)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            row["product_name"],
            row["category"],
            row["brand"],
            row["price"],
            row["stock_quantity"]
        )
    )

# Save Changes
connection.commit()

# Close Connection
connection.close()

print("✅ Products Imported Successfully!")