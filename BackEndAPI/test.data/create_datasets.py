import requests
import random
import uuid

# Define the API endpoints
users_api_url = "http://localhost:8000/users/"
datasets_api_url = "http://localhost:8000/datasets/"

# Function to create a dataset
def create_dataset(name, description, images, owner_id):
    dataset_data = {
        "name": name,
        "description": description,
        "images": images,
        "owner_id": owner_id
    }
    response = requests.post(datasets_api_url, json=dataset_data)
    if response.status_code == 201:
        print(f"Dataset created for user {owner_id}: {name}")
    else:
        print(f"Failed to create dataset for user {owner_id}, Status Code: {response.status_code}, Response: {response.text}")

# Retrieve the list of users
response = requests.get(users_api_url)
if response.status_code == 200:
    users = response.json()
    for user in users:
        user_id = user['id']
        num_datasets = random.randint(1, 10)
        for i in range(num_datasets):
            dataset_name = f"Dataset {i+1} for {user['name']}"
            dataset_description = f"Description for dataset {i+1} of {user['name']}"
            dataset_images = f"/path/to/images/{uuid.uuid4().hex[:8]}"
            create_dataset(dataset_name, dataset_description, dataset_images, user_id)
else:
    print(f"Failed to retrieve users, Status Code: {response.status_code}, Response: {response.text}")