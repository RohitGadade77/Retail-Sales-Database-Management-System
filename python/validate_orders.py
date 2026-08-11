import pandas as pd

# Read CSV
df = pd.read_csv("data/orders.csv")

print("========== INFO ==========")
print(df.info())

print("\n========== NULL VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE ORDERS ==========")
print(df.duplicated().sum())

print("\n========== CUSTOMER ID RANGE ==========")
print(
    "Min:", df["customer_id"].min(),
    "Max:", df["customer_id"].max()
)

print("\n========== PRODUCT ID RANGE ==========")
print(
    "Min:", df["product_id"].min(),
    "Max:", df["product_id"].max()
)

print("\n========== TOTAL RECORDS ==========")
print(len(df))