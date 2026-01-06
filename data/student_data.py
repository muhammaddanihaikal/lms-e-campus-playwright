from faker import Faker
import random
from datetime import datetime

fake = Faker('id_ID')

def student_data():
    name = f"studentex{random.randint(100, 999)}"
    email = f"{name}@example.com"

    return {
        # Informasi Pribadi
        "full_name": name,
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
        "study_program": "44", # Artificial Intelligence
        "entry_year": str(datetime.now().year),
        "degree": "S1 (Bachelor)",
        "current_semester": "1",
        "class_type": "Regular",
        "entry_path": "regular",
        "status": "active",

        # account
        "username": name,
        "password": "12345678"
    }
