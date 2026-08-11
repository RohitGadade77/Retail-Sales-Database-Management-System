CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    city VARCHAR(50),
    state VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);