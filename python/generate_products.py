import pandas as pd
import random

product_names = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor",
    "Headphones",
    "Smartphone",
    "Tablet",
    "Printer",
    "Camera",
    "Smartwatch",
    "T-Shirt",
    "Jeans",
    "Shoes",
    "Backpack",
    "Bottle",
    "Notebook",
    "Pen",
    "Football",
    "Cricket Bat",
    "Rice Bag"
]

categories = [
    "Electronics",
    "Fashion",
    "Sports",
    "Books",
    "Grocery"
]

brands = [
    "Samsung",
    "HP",
    "Dell",
    "Nike",
    "Adidas",
    "Puma",
    "Sony",
    "Apple",
    "Boat",
    "Classmate"
]

products = []

for i in range(50):

    product = {
        "product_name": random.choice(product_names),
        "category": random.choice(categories),
        "brand": random.choice(brands),
        "price": round(random.uniform(100, 50000), 2),
        "stock_quantity": random.randint(5, 300)
    }

    products.append(product)

    df = pd.DataFrame(products)

    df.to_csv("data/products.csv", index=False)

print(df)

print("\n✅ products.csv created successfully!")