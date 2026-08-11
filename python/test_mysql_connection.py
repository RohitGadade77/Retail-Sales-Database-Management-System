import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="retail_sales_db"
)

print("✅ Connected Successfully!")

connection.close()