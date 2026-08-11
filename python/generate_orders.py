import pandas as pd
import random

orders = []

for i in range(100):

    order = {
        "customer_id": random.randint(1, 50),
        "product_id": random.randint(1, 50),
        "quantity": random.randint(1, 5),
        "order_date": f"2026-{random.randint(1,12):02d}-{random.randint(1,28):02d}"
    }

    orders.append(order)

    df = pd.DataFrame(orders)

    df.to_csv("data/orders.csv", index=False)

print(df)

print("\n✅ orders.csv created successfully!")