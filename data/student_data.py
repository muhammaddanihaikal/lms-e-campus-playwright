from faker import Faker
import random
from datetime import datetime

fake = Faker('id_ID')

def student_data():
    base_name = f"{fake.first_name().lower()}"[:5]  # Max 5 huruf
    username = f"{base_name}es"
    email = f"{username}@gmail.com"
    full_name = f"{base_name.capitalize()} ES"

    return {
        # Personal Info Tab
        "full_name": full_name,
        "email": email,
        "nisn": fake.numerify(text='##########'),
        "gender": random.choice(["Male", "Female"]),
        "religion": "Islam",
        "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=25).strftime("%Y-%m-%d"),
        "place_of_birth": fake.city(),
        "phone": fake.phone_number(),
        "address": fake.address(),

        # Family & Emergency Tab
        "parent_name": fake.name(),
        "parent_phone": fake.phone_number(),
        "contact_name": fake.name(),
        "contact_phone": fake.phone_number(),
        "relationship": "Parent",

        # Education & Academic Tab
        "high_school": f"SMA {fake.city()}",
        "grad_year": "2024",
        "prev_education": "Senior High School (SMA/SMK)",
        "department": "49",
        "semester": "1",
        "degree": "S1 (Bachelor)",
        "class_type": "Regular",
        "entry_path": "Regular",

        # account
        "username": username,
        "password": "12345678"
    }
