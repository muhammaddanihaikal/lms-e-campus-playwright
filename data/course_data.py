from faker import Faker
import random

fake = Faker('id_ID')

def course_data():
    course_name = fake.catch_phrase()
    
    return {
        # course information
        "course_name": course_name,
        "course_description": fake.paragraph(),

        # academic information
        "faculty": "School of Information Systems",
        "department": "Business Information Systems",
        "semester": "Odd",
        "status": "Active",

        # assessment indicators
        "indicator_name": "UAS",
        "indicator_weight": "100",

        # learning outcomes
        "learning_outcome": fake.sentence(),

        # textbooks & references
        "textbook_title": fake.catch_phrase(),
        "textbook_author": fake.name(),
        "textbook_publisher": fake.company(),
        "textbook_year": str(random.randint(2010, 2025)),

        # teaching strategies
        "strategy": fake.sentence(),

        # prerequisites
        "prerequisite": fake.catch_phrase(),

        # contact & office hours
        "contact_email": fake.email(),
        "office_hours": "Monday & Wednesday 2-4 PM",

        # course policies
        "attendance_policy": "Minimum 75% attendance required.",
        "late_submission_policy": "10% deduction per day.",
        "academic_integrity": "Plagiarism is strictly prohibited.",
        "communication_policy": "Contact via email or LMS forum.",
    }
