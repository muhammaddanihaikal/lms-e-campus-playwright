from faker import Faker
import random
from config.config import BASE_DIR

fake = Faker('id_ID')

def admission_data():
    base_name = fake.first_name().lower()
    username = f"{base_name}bis"
    email = f"{username}@gmail.com"
    full_name = f"{base_name.capitalize()} BIS"

    return {
        # ===== Data Pribadi =====
        "full_name": full_name,
        "nisn": fake.numerify(text='##########'),  # 10 digit nomor acak
        "gender": random.choice(["Male", "Female"]),
        "religion": "Islam", 
        "place_of_birth": fake.city(),
        "date_of_birth": fake.date_of_birth(minimum_age=15, maximum_age=19).strftime("%Y-%m-%d"),
        "address": fake.address(),
        "email": email,
        "phone": fake.phone_number(),

        # ===== Orang Tua / Wali =====
        "parent_name": fake.name(),
        "parent_phone": fake.phone_number(),
        "parent_email": fake.email(),

        # ===== Kontak Darurat =====
        "emergency_name": fake.name(),
        "emergency_phone": fake.phone_number(),
        "relationship": "Parent",

        # ===== Pendidikan =====
        "high_school": f"SMA {fake.city()}",
        "graduation_year": "2024",
        "education_level": "Senior High School (SMA/SMK)",

        # ===== Pilihan Program Studi =====
        "study_program": "Business Information Systems (ISBIS) - S1",
        "entry_year": "2026",
        "class_type": "Regular",
        "entry_path": "regular",

        # ===== Dokumen =====
        "academic_transcript": BASE_DIR / "test_file" / "test_pdf_150kb.pdf",
        "diploma": BASE_DIR / "test_file" / "test_pdf_150kb.pdf",
        "national_id": BASE_DIR / "test_file" / "test_pdf_150kb.pdf",
        "family_card": BASE_DIR / "test_file" / "test_pdf_150kb.pdf",
    }
