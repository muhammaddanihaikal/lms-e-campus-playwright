import random
from faker import Faker
from datetime import datetime

fake = Faker('id_ID')

def kaprodi_data():
    name = f"kaprodiex{random.randint(100, 999)}"
    email = f"{name}@example.com"
    
    return {
        "kaprodi_name": name,
        "email": email,
        "phone_number": fake.phone_number(),
        "entry_year": str(datetime.now().year),
        "gender": random.choice(["Male", "Female"]),
        "religion": "Islam",
        "date_of_birth": fake.date_of_birth(minimum_age=30, maximum_age=65).strftime("%Y-%m-%d"),
        "place_of_birth": fake.city(),
        "faculty": "School of Computer Science",
        "department": "Artificial Intelligence",

        # account
        "username": name,
        "password": "12345678"
    }