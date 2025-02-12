import requests
import random
import uuid

# Define the API endpoint
api_url = "http://localhost:8000/users/"

# List of real names
names = [
    "Alice Johnson", "Bob Smith", "Charlie Brown", "David Wilson", "Eve Davis",
    "Frank Miller", "Grace Lee", "Hank Harris", "Ivy Clark", "Jack Lewis",
    "Kathy Walker", "Liam Hall", "Mia Allen", "Noah Young", "Olivia King",
    "Paul Wright", "Quinn Scott", "Ruby Green", "Sam Adams", "Tina Baker",
    "Uma Nelson", "Victor Carter", "Wendy Mitchell", "Xander Perez", "Yara Roberts",
    "Zane Turner", "Ava Phillips", "Ben Campbell", "Chloe Parker", "Dylan Evans",
    "Ella Edwards", "Finn Collins", "Gina Stewart", "Henry Morris", "Isla Rogers",
    "Jake Reed", "Lily Cook", "Mason Morgan", "Nina Bell", "Oscar Murphy",
    "Piper Bailey", "Quincy Rivera", "Riley Cooper", "Sophie Richardson", "Tyler Cox",
    "Violet Howard", "Wyatt Ward", "Zoe Brooks", "Aaron Sanders", "Bella Price",
    "Caleb Bennett", "Daisy Wood", "Ethan Barnes", "Fiona Ross", "Gavin Henderson",
    "Holly Coleman", "Ian Jenkins", "Jade Perry", "Kyle Powell", "Luna Long",
    "Miles Patterson", "Nora Hughes", "Owen Flores", "Paige Washington", "Ryan Butler",
    "Sara Simmons", "Theo Foster", "Vera Gonzales", "Will Russell", "Xena Griffin",
    "Yusuf Diaz", "Zara Hayes", "Adam Myers", "Brooke Ford", "Cody Hamilton",
    "Diana Graham", "Eli Fisher", "Faith Wallace", "George Woods", "Hannah West",
    "Isaac Stone", "Jenna Bryant", "Kevin Spencer", "Leah Warren", "Max Hunter",
    "Nadia Gibson", "Oliver Matthews", "Penny Shaw", "Quinn Black", "Rory Daniels",
    "Sienna Palmer", "Toby Ellis", "Vince Franklin", "Willa Jordan", "Xavier Lawson",
    "Yasmine Weaver", "Zachary Chapman"
]

# Function to create a user
def create_user(email, name, description):
    user_data = {
        "email": email,
        "name": name,
        "description": description
    }
    response = requests.post(api_url, json=user_data)
    if response.status_code == 201:
        print(f"User created: {email}")
    else:
        print(f"Failed to create user: {email}, Status Code: {response.status_code}, Response: {response.text}")

# Create 100 users
for name in names:
    email = f"{name.split()[0].lower()}.{name.split()[1].lower()}{random.randint(1, 100)}@example.com"
    description = f"Description for {name}"
    create_user(email, name, description)
    
    
