import pandas as pd

df = pd.read_csv("data/customers.csv")

print("========== INFO ==========")
df.info()

print("\n========== NULL VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE EMAILS ==========")
print(df["email"].duplicated().sum())

print("\n========== DUPLICATE PHONE ==========")
print(df["phone"].duplicated().sum())

print("\n========== TOTAL RECORDS ==========")
print(len(df))