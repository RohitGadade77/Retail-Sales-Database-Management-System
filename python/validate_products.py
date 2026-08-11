import pandas as pd

# Read CSV
df = pd.read_csv("data/products.csv")

print("========== INFO ==========")
print(df.info())

print("\n========== NULL VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE PRODUCTS ==========")
print(df["product_name"].duplicated().sum())

print("\n========== TOTAL RECORDS ==========")
print(len(df))