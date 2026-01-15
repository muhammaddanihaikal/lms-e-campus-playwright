from faker import Faker
import random
from datetime import datetime

fake = Faker('id_ID')

def student_data():
    base_name = fake.first_name().lower()
    username = f"{base_name}bis"
    email = f"{username}@gmail.com"
    full_name = f"{base_name.capitalize()} BIS"

    return {
        # Informasi Pribadi
        "full_name": full_name,
        "email": email,
        "nisn": fake.numerify(text='##########'),
        "gender": random.choice(["Male", "Female"]),
        "religion": "Islam",
        "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=25).strftime("%Y-%m-%d"),
        "place_of_birth": fake.city(),
        "phone": fake.phone_number(),
        "address": fake.address(),

        # Informasi Orang Tua/Wali
        "parent_name": fake.name(),
        "parent_phone": fake.phone_number(),
        "parent_email": fake.email(),

        # Kontak Darurat
        "emergency_name": fake.name(),
        "emergency_phone": fake.phone_number(),
        "relationship": "Parent",

        # Latar Belakang Pendidikan
        "high_school": f"SMA {fake.city()}",
        "graduation_year": "2024",
        "education_level": "Senior High School (SMA/SMK)",

        # Informasi Akademik
        "study_program": "Business Information Systems",
        "entry_year": "2026",
        "degree": "S1 (Bachelor)",
        "current_semester": "1",
        "class_type": "Regular",
        "entry_path": "regular",
        "status": "active",

        # account
        "username": username,
        "password": "12345678"
    }
