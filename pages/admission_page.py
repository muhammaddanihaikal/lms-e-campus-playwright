from playwright.sync_api import Page
from config.config import BASE_URL


class AdmissionPage:
    def __init__(self, page: Page):
        self.page = page

        # Data Pribadi
        self.full_name = page.get_by_role("textbox", name="Full Name")
        self.nisn = page.get_by_role("textbox", name="National Student ID (NISN)")
        self.gender = page.get_by_label("Gender*")
        self.religion = page.get_by_label("Religion*")
        self.place_of_birth = page.get_by_role("textbox", name="Place of Birth")
        self.date_of_birth = page.get_by_role("textbox", name="Date of Birth")
        self.address = page.get_by_role("textbox", name="Complete Address")
        self.email = page.get_by_role("textbox", name="Email Address")
        self.phone = page.get_by_role("textbox", name="Phone Number")

        # Orang Tua / Wali
        self.parent_name = page.get_by_role("textbox", name="Parent/Guardian Name")
        self.parent_phone = page.get_by_role("textbox", name="Parent/Guardian Phone")
        self.parent_email = page.get_by_role("textbox", name="Parent/Guardian Email")

        # Kontak Darurat
        self.emergency_name = page.get_by_role("textbox", name="Emergency Contact Name")
        self.emergency_phone = page.get_by_role("textbox", name="Emergency Contact Phone")
        self.relationship = page.get_by_label("Relationship*")

        # Pendidikan
        self.high_school = page.get_by_role("textbox", name="High School Name")
        self.graduation_year = page.get_by_label("Graduation Year*")
        self.education_level = page.get_by_label("Previous Education Level*")

        # Pilihan Program Studi
        self.study_program = page.get_by_label("Study Program*")
        self.class_type = page.get_by_label("Class Type*")
        self.entry_path = page.get_by_label("Entry Path*")

        # ===== Dokumen Pendukung =====
        self.academic_transcript = page.locator('input[name="report"]')
        self.diploma = page.locator('input[name="certificate"]')
        self.national_id = page.locator('input[name="idCard"]')
        self.family_card = page.locator('input[name="familyCard"]')

        # Tombol Submit
        self.submit_btn = page.get_by_role("button", name="Submit Application")

    def open(self):
        self.page.goto(f"{BASE_URL}/login")
        self.page.get_by_role("link", name="Admission").click()
    
    def submit(self, data):
        # ===== Data Pribadi =====
        self.full_name.fill(data["full_name"])
        self.nisn.fill(data["nisn"])
        self.gender.select_option(data["gender"])
        self.religion.select_option(data["religion"])
        self.place_of_birth.fill(data["place_of_birth"])
        self.date_of_birth.fill(data["date_of_birth"])
        self.address.fill(data["address"])
        self.email.fill(data["email"])
        self.phone.fill(data["phone"])

        # ===== Orang Tua / Wali =====
        self.parent_name.fill(data["parent_name"])
        self.parent_phone.fill(data["parent_phone"])
        self.parent_email.fill(data["parent_email"])

        # ===== Kontak Darurat =====
        self.emergency_name.fill(data["emergency_name"])
        self.emergency_phone.fill(data["emergency_phone"])
        self.relationship.select_option(data["relationship"])

        # ===== Pendidikan =====
        self.high_school.fill(data["high_school"])
        self.graduation_year.select_option(data["graduation_year"])
        self.education_level.select_option(data["education_level"])

        # ===== Pilihan Program Studi =====
        self.study_program.select_option(data["study_program"])
        self.class_type.select_option(data["class_type"])
        self.entry_path.select_option(data["entry_path"])

        # ===== Dokumen Pendukung =====
        self.academic_transcript.set_input_files(data["academic_transcript"])
        self.diploma.set_input_files(data["diploma"])
        self.national_id.set_input_files(data["national_id"])
        self.family_card.set_input_files(data["family_card"])

        # ===== Kirim =====
        self.submit_btn.click()
