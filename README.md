Retail Sales Database Management System
📌 Project Overview

The Retail Sales Database Management System is a data engineering project that manages retail sales data using Python, Pandas, MySQL, and SQL.

The project demonstrates an end-to-end data pipeline where data is generated and stored in CSV files, validated and transformed using Python, and finally loaded into a relational MySQL database for analysis.

🛠️ Technologies Used
Python 3.12
Pandas
MySQL
MySQL Connector/Python
SQL
Git & GitHub
VS Code
MySQL Workbench
🔄 ETL Pipeline

The project implements a basic ETL (Extract, Transform, Load) pipeline.

CSV Files
    ↓
Extract
Python + Pandas
    ↓
Transform
Data Validation
Null & Duplicate Checks
Data Processing
    ↓
Load
Python + MySQL Connector
    ↓
MySQL Database
Extract

Data is generated and stored in CSV files:

customers.csv
products.csv
orders.csv

Python and Pandas are used to read the CSV data.

Transform

The data is validated before loading into MySQL.

Validation includes:

Null value checks
Duplicate checks
Record count validation
Data type validation
Customer and Product ID validation

For orders, total_amount is calculated using:

Total Amount = Product Price × Quantity
Load

The processed data is loaded into MySQL using mysql-connector-python.

🗄️ Database Structure

The database contains three main tables:

Customers

Stores customer information.

customer_id
first_name
last_name
email
phone
city
state
created_at
Products

Stores product information.

product_id
product_name
category
brand
price
stock_quantity
created_at
Orders

Stores customer purchase information.

order_id
customer_id
product_id
quantity
order_date
total_amount
Relationships
Customers
    │
    │ customer_id
    ▼
 Orders
    ▲
    │ product_id
    │
Products
orders.customer_id → customers.customer_id
orders.product_id → products.product_id

Foreign key constraints maintain data integrity.

📊 SQL Analysis

SQL queries are used to analyze the retail sales data.

The project includes queries for:

Total customers
Total products
Total orders
Total revenue
Average order value
Customer order analysis
Product sales analysis
Top-selling products
Top customers by spending
Quantity sold by product
JOIN operations
GROUP BY analysis
Aggregate functions

SQL concepts demonstrated:

SELECT
JOIN
GROUP BY
ORDER BY
WHERE
SUM()
COUNT()
AVG()
LIMIT
📁 Project Structure
Retail-Sales-Database-Management-System/
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   └── orders.csv
│
├── python/
│   ├── generate_customers.py
│   ├── validate_customers.py
│   ├── import_customers.py
│   ├── generate_products.py
│   ├── validate_products.py
│   ├── import_products.py
│   ├── generate_orders.py
│   ├── validate_orders.py
│   ├── import_orders.py
│   └── test_mysql_connection.py
│
├── sql/
│   ├── 01_create_database.sql
│   ├── 02_create_customers_table.sql
│   ├── 03_create_products_table.sql
│   ├── 04_create_orders_table.sql
│   └── 05_reports.sql
│
├── screenshots/
│   ├── customers_table.png
│   ├── products_table.png
│   └── order_table.png
│
└── README.md
⚙️ How to Run
1. Clone the Repository
git clone git@github.com:RohitGadade77/Retail-Sales-Database-Management-System.git
2. Install Required Python Libraries
pip install pandas mysql-connector-python
3. Create the Database

Run:

sql/01_create_database.sql

in MySQL Workbench.

4. Create Tables

Run the following SQL files:

02_create_customers_table.sql
03_create_products_table.sql
04_create_orders_table.sql
5. Generate CSV Data

Run:

python python/generate_customers.py
python python/generate_products.py
python python/generate_orders.py
6. Validate Data
python python/validate_customers.py
python python/validate_products.py
python python/validate_orders.py
7. Load Data into MySQL
python python/import_customers.py
python python/import_products.py
python python/import_orders.py
8. Run SQL Reports

Open:

sql/05_reports.sql

in MySQL Workbench and execute the queries.

📸 Screenshots

Project screenshots are available in the screenshots/ folder and demonstrate the database tables and imported data.

🎯 Key Learning Outcomes

Through this project, I implemented:

Relational database design
Primary and foreign keys
CSV data processing
Data validation using Pandas
Python-to-MySQL connectivity
ETL pipeline implementation
SQL JOIN operations
SQL aggregation and reporting
Data integrity using foreign keys
Git and GitHub version control
👨‍💻 Author

Rohit Gadade

MCA Student | Aspiring Data Engineer