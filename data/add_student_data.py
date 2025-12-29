from faker import Faker
import random
from datetime import datetime

fake = Faker('id_ID')

def add_student_data():
    generated_name = fake.name()
    # Pembuatan username sederhana dari nama
    username = generated_name.replace(' ', '').lower()[:10] + str(random.randint(100, 999))
    email = f"{username}@example.com"

    return {
        # ===== Informasi Pribadi =====
        "full_name": generated_name,
        "username": username,
        "email": email,
        "nisn": fake.numerify(text='##########'),
        "gender": random.choice(["Male", "Female"]),
        "religion": "Islam",
        "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=25).strftime("%Y-%m-%d"),
        "place_of_birth": fake.city(),
        "phone": fake.phone_number(),
        "address": fake.address(),

        # ===== Informasi Orang Tua/Wali =====
        "parent_name": fake.name(),
        "parent_phone": fake.phone_number(),
        "parent_email": fake.email(),

        # ===== Kontak Darurat =====
        "emergency_name": fake.name(),
        "emergency_phone": fake.phone_number(),
        "relationship": "Parent",

        # ===== Latar Belakang Pendidikan =====
        "high_school": f"SMA {fake.city()}",
        "graduation_year": "2024",
        "education_level": "Senior High School (SMA/SMK)",

        # ===== Informasi Akademik =====
        "study_program": "56", # Contoh Informatika
        "entry_year": str(datetime.now().year),
        "degree": "S1 (Bachelor)",
        "current_semester": "1",
        "class_type": "Regular",
        "entry_path": "regular",
        "status": "active",
    }
