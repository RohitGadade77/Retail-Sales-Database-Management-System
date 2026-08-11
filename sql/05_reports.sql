-- =========================================
-- RETAIL SALES DATABASE REPORTS
-- =========================================

-- Total Customers
SELECT COUNT(*) AS Total_Customers
FROM customers;

-- Total Products
SELECT COUNT(*) AS Total_Products
FROM products;

-- Total Orders
SELECT COUNT(*) AS Total_Orders
FROM orders;

-- View Customers
SELECT * FROM customers;

-- View Products
SELECT * FROM products;

-- View Orders
SELECT * FROM orders;

-- Customer Orders
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    o.order_id,
    o.order_date,
    o.quantity,
    o.total_amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;

-- Product Orders
SELECT
    p.product_name,
    p.category,
    o.quantity,
    o.total_amount
FROM products p
JOIN orders o
ON p.product_id = o.product_id;

-- Total Orders per Customer
SELECT
    customer_id,
    COUNT(*) AS Total_Orders
FROM orders
GROUP BY customer_id;

-- Total Quantity Sold per Product
SELECT
    product_id,
    SUM(quantity) AS Total_Sold
FROM orders
GROUP BY product_id;

-- Total Revenue
SELECT
SUM(total_amount) AS Total_Revenue
FROM orders;

-- Average Order Value
SELECT
AVG(total_amount) AS Average_Order_Value
FROM orders;

-- Top 5 Selling Products
SELECT
    p.product_name,
    SUM(o.quantity) AS Total_Sold
FROM products p
JOIN orders o
ON p.product_id = o.product_id
GROUP BY p.product_name
ORDER BY Total_Sold DESC
LIMIT 5;

-- Top 5 Customers by Spending
SELECT
    c.first_name,
    c.last_name,
    SUM(o.total_amount) AS Total_Spent
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY Total_Spent DESC
LIMIT 5;