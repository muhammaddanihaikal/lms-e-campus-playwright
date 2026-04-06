from faker import Faker
import random

fake = Faker('id_ID')

def course_data():
    es_courses = [
    "Enterprise Systems",
    "ERP Basics",
    "ERP Implementation",
    "SAP Fundamentals",
    "Enterprise Architecture",
    "Business Processes",
    "Process Modeling",
    "Enterprise Integration",
    "System Integration",
    "Enterprise Data",

    "Enterprise Applications",
    "Enterprise Software",
    "Business Information Systems",
    "Management Information Systems",
    "Decision Support Systems",
    "Supply Chain Systems",
    "Customer Relationship Management",
    "CRM Systems",
    "Enterprise Analytics",
    "Business Analytics",

    "Enterprise Databases",
    "Data Warehousing",
    "Enterprise Reporting",
    "IT Governance",
    "IT Service Management",
    "COBIT Framework",
    "ITIL Fundamentals",
    "Digital Enterprise",
    "Enterprise Cloud",
    "Cloud ERP",

    "Enterprise Security",
    "Risk Management",
    "Compliance Systems",
    "Business Continuity",
    "Enterprise Automation",
    "Robotic Process Automation",
    "Enterprise DevOps",
    "Enterprise Integration Patterns",
    "Enterprise APIs",
    "Enterprise Middleware",

    "Enterprise Project Management",
    "Change Management",
    "Enterprise Strategy",
    "Business Transformation",
    "Enterprise Planning",
    "Enterprise Innovation"
    ]

    course_name = random.choice(es_courses)
    
    return {
        # course information
        "course_name": course_name,
        "course_description": fake.paragraph(),

        # academic information
        "faculty": "School of Information Systems",
        "department": "Enterprise Systems",
        "semester": "Odd",
        "credits_distribution": 0,
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
