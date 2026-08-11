import pandas as pd
import mysql.connector

# Read CSV
df = pd.read_csv("data/customers.csv")

# Connect MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="retail_sales_db"
)

cursor = connection.cursor()

print("✅ CSV Read Successfully")
print("✅ MySQL Connected Successfully")

# Insert data
for index, row in df.iterrows():

    cursor.execute(
        """
        INSERT INTO customers
        (first_name, last_name, email, phone, city, state)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (
            row["first_name"],
            row["last_name"],
            row["email"],
            row["phone"],
            row["city"],
            row["state"]
        )
    )

# Save changes
connection.commit()

# Close connection
connection.close()

print("✅ Customers Imported Successfully!")