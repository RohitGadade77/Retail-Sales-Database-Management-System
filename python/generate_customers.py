import pandas as pd

first_names = [
    "Rohit", "Amit", "Priya", "Sneha", "Akash",
    "Pooja", "Rahul", "Neha", "Karan", "Anjali",
    "Vishal", "Sakshi", "Abhishek", "Aarti", "Nikhil",
    "Komal", "Sagar", "Vaishnavi", "Om", "Rutuja",
    "Ajay", "Swati", "Pratik", "Shreya", "Tejas",
    "Snehal", "Yash", "Tanvi", "Harshal", "Monika",
    "Saurabh", "Prajakta", "Ganesh", "Riya", "Aditya",
    "Payal", "Sanket", "Kajal", "Shubham", "Pallavi",
    "Aniket", "Sayali", "Tushar", "Pritam", "Aishwarya",
    "Nilesh", "Bhagyashree", "Rohan", "Dipali", "Ashwini"
]

last_names = [
    "Patil", "Sharma", "Kulkarni", "Joshi", "Deshmukh",
    "Pawar", "Jadhav", "Shinde", "More", "Kadam"
]

cities = [
    "Pune", "Mumbai", "Nashik", "Nagpur", "Kolhapur",
    "Sangli", "Satara", "Solapur", "Aurangabad", "Thane"
]

customers = []

for i in range(50):
    customers.append({
        "customer_id": i + 1,
        "first_name": first_names[i],
        "last_name": last_names[i % len(last_names)],
        "email": f"{first_names[i].lower()}{i+1}@gmail.com",
        "phone": f"98{76543210 + i}",
        "city": cities[i % len(cities)],
        "state": "Maharashtra"
    })

df = pd.DataFrame(customers)

df.to_csv("data/customers.csv", index=False)

print(df)

print("\n✅ customers.csv created successfully!")