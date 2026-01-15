import random
from faker import Faker
from datetime import datetime

fake = Faker('id_ID')

def lecturer_data():
    base_name = fake.first_name().lower()
    username = f"{base_name}BIS"
    email = f"{base_name}@gmail.com"
    full_name = f"{base_name.capitalize()} BIS"
    
    return {
        "lecturer_name": full_name,
        "email": email,
        "phone_number": fake.phone_number(),
        "entry_year": str(datetime.now().year),
        "gender": random.choice(["Male", "Female"]),
        "religion": "Islam",
        "date_of_birth": fake.date_of_birth(minimum_age=25, maximum_age=60).strftime("%Y-%m-%d"),
        "place_of_birth": fake.city(),
        "faculty": "School of Information Systems",
        "department": "Business Information Systems",

        # account
        "username": username,
        "password": "12345678",
        "confirm_password": "12345678"
    }
