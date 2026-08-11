import pandas as pd
import mysql.connector

# Read CSV
df = pd.read_csv("data/orders.csv")

# Connect MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="retail_sales_db"
)

cursor = connection.cursor()

print("✅ Orders CSV Read Successfully")
print("✅ MySQL Connected Successfully")

# Insert Orders
for index, row in df.iterrows():

    # Get product price
    cursor.execute(
        "SELECT price FROM products WHERE product_id = %s",
        (row["product_id"],)
    )

    result = cursor.fetchone()

    if result is None:
        print(f"❌ Product ID {row['product_id']} not found.")
        continue

    price = float(result[0])

    # Calculate Total Amount
    total_amount = price * row["quantity"]

    # Insert Order
    cursor.execute(
        """
        INSERT INTO orders
        (customer_id, product_id, quantity, order_date, total_amount)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            row["customer_id"],
            row["product_id"],
            row["quantity"],
            row["order_date"],
            total_amount
        )
    )

# Save Changes
connection.commit()

# Close Connection
cursor.close()
connection.close()

print("✅ Orders Imported Successfully!")