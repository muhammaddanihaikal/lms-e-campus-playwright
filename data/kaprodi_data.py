import random
from faker import Faker
from datetime import datetime

fake = Faker('id_ID')

def kaprodi_data():
    base_name = f"kaprodi"
    username = f"{base_name}es"
    email = f"{username}@gmail.com"
    name = f"{base_name} ES"
    
    return {
        "kaprodi_name": name,
        "email": email,
        "phone_number": f"08{random.randint(1000000000, 9999999999)}",
        "entry_year": str(datetime.now().year),
        "gender": random.choice(["Male", "Female"]),
        "religion": "Islam",
        "date_of_birth": fake.date_of_birth(minimum_age=30, maximum_age=65).strftime("%Y-%m-%d"),
        "place_of_birth": fake.city(),
        "faculty": "School of Information Systems",
        "department": "Enterprise Systems",

        # account
        "username": username,
        "password": "12345678"
    }