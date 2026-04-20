"""Faker helpers untuk generate data dinamis (unique tiap test)."""

import random
from datetime import datetime

from faker import Faker

fake = Faker("id_ID")


def generate_student():
    base_name = fake.first_name().lower()[:5]
    username = f"{base_name}es"
    email = f"{username}@gmail.com"
    full_name = f"{base_name.capitalize()} ES"

    return {
        "full_name": full_name,
        "email": email,
        "nisn": fake.numerify(text="##########"),
        "gender": random.choice(["Male", "Female"]),
        "religion": "Islam",
        "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=25).strftime("%Y-%m-%d"),
        "place_of_birth": fake.city(),
        "phone": fake.phone_number(),
        "address": fake.address(),
        "parent_name": fake.name(),
        "parent_phone": fake.phone_number(),
        "contact_name": fake.name(),
        "contact_phone": fake.phone_number(),
        "relationship": "Parent",
        "high_school": f"SMA {fake.city()}",
        "grad_year": "2024",
        "prev_education": "Senior High School (SMA/SMK)",
        "department": "49",
        "semester": "1",
        "degree": "S1 (Bachelor)",
        "class_type": "Regular",
        "entry_path": "Regular",
        "username": username,
        "password": "12345678",
    }


def generate_kaprodi():
    base_name = "kaprodi"
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
        "username": username,
        "password": "12345678",
    }


def generate_lecturer():
    base_name = fake.first_name().lower()[:5]
    username = f"{base_name}es"
    email = f"{username}@gmail.com"
    full_name = f"Dosen {base_name.capitalize()} ES"

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
        "department": "Enterprise Systems",
        "username": username,
        "password": "12345678",
        "confirm_password": "12345678",
    }


def generate_course():
    es_courses = [
        "Enterprise Systems", "ERP Basics", "ERP Implementation", "SAP Fundamentals",
        "Enterprise Architecture", "Business Processes", "Process Modeling",
        "Enterprise Integration", "System Integration", "Enterprise Data",
        "Enterprise Applications", "Enterprise Software", "Business Information Systems",
        "Management Information Systems", "Decision Support Systems", "Supply Chain Systems",
        "Customer Relationship Management", "CRM Systems", "Enterprise Analytics",
        "Business Analytics", "Enterprise Databases", "Data Warehousing",
        "Enterprise Reporting", "IT Governance", "IT Service Management",
        "COBIT Framework", "ITIL Fundamentals", "Digital Enterprise",
        "Enterprise Cloud", "Cloud ERP", "Enterprise Security", "Risk Management",
        "Compliance Systems", "Business Continuity", "Enterprise Automation",
        "Robotic Process Automation", "Enterprise DevOps", "Enterprise Integration Patterns",
        "Enterprise APIs", "Enterprise Middleware", "Enterprise Project Management",
        "Change Management", "Enterprise Strategy", "Business Transformation",
        "Enterprise Planning", "Enterprise Innovation",
    ]

    return {
        "course_name": random.choice(es_courses),
        "course_description": fake.paragraph(),
        "faculty": "School of Information Systems",
        "department": "Enterprise Systems",
        "semester": "Odd",
        "credits_distribution": 0,
        "status": "Active",
        "indicator_name": "UAS",
        "indicator_weight": "100",
        "learning_outcome": fake.sentence(),
        "textbook_title": fake.catch_phrase(),
        "textbook_author": fake.name(),
        "textbook_publisher": fake.company(),
        "textbook_year": str(random.randint(2010, 2025)),
        "strategy": fake.sentence(),
        "prerequisite": fake.catch_phrase(),
        "contact_email": fake.email(),
        "office_hours": "Monday & Wednesday 2-4 PM",
        "attendance_policy": "Minimum 75% attendance required.",
        "late_submission_policy": "10% deduction per day.",
        "academic_integrity": "Plagiarism is strictly prohibited.",
        "communication_policy": "Contact via email or LMS forum.",
    }


def generate_admission(base_dir):
    base_name = fake.first_name().lower()
    username = f"{base_name}es"
    email = f"{username}@gmail.com"
    full_name = f"{base_name.upper()} ES"

    return {
        "full_name": full_name,
        "nisn": fake.numerify(text="##########"),
        "gender": random.choice(["Male", "Female"]),
        "religion": "Islam",
        "place_of_birth": fake.city(),
        "date_of_birth": fake.date_of_birth(minimum_age=15, maximum_age=19).strftime("%Y-%m-%d"),
        "address": fake.address(),
        "email": email,
        "phone": fake.phone_number(),
        "parent_name": fake.name(),
        "parent_phone": fake.phone_number(),
        "parent_email": fake.email(),
        "emergency_name": fake.name(),
        "emergency_phone": fake.phone_number(),
        "relationship": "Parent",
        "high_school": f"SMA {fake.city()}",
        "graduation_year": "2024",
        "education_level": "Senior High School (SMA/SMK)",
        "study_program": "Dept. of Software Engineering (SE-FCS-101) - S1",
        "entry_year": "2026",
        "class_type": "Regular",
        "entry_path": "regular",
        "academic_transcript": base_dir / "test_file" / "test_pdf_150kb.pdf",
        "diploma": base_dir / "test_file" / "test_pdf_150kb.pdf",
        "national_id": base_dir / "test_file" / "test_pdf_150kb.pdf",
        "family_card": base_dir / "test_file" / "test_pdf_150kb.pdf",
    }


def generate_thesis_proposal(student_name: str = "student"):
    return {
        "thesis_track": "Thesis",
        "thesis_title": f"Tesis Sistem Informasi {student_name}",
        "research_background": "Sistem informasi penting untuk efisiensi bisnis modern",
        "research_objectives": "Menganalisis dampak sistem informasi terhadap produktivitas",
        "methodology": "Kualitatif dengan studi kasus",
    }
