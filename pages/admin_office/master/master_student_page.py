from playwright.sync_api import Page, expect
from config.config import BASE_URL
from datetime import datetime

class MasterStudentPage:
    def __init__(self, page: Page):
        self.page = page

        # Navigasi
        self.master_menu = page.get_by_text("Master", exact=True).first
        self.master_student_menu = page.locator("a").filter(has_text="Master Student")
        self.add_new_student_btn = page.get_by_role("button", name="Add New Student")
        self.details_btn = page.get_by_role("button", name="Details")
        self.delete_btn = page.get_by_role("button", name="Delete")

        # 1. Informasi Pribadi
        self.full_name = page.get_by_role("textbox", name="Full Name")
        self.username = page.get_by_role("textbox", name="Username") 
        self.email = page.get_by_role("textbox", name="Personal Email")
        self.nisn = page.get_by_role("textbox", name="National Student ID (NISN)")
        self.gender = page.get_by_label("Gender")
        self.religion = page.get_by_label("Religion")
        self.date_of_birth = page.get_by_role("textbox", name="Date of Birth")
        self.place_of_birth = page.get_by_role("textbox", name="Place of Birth")
        self.phone = page.get_by_role("textbox", name="Phone Number")
        self.address = page.get_by_role("textbox", name="Complete Address")

        # 2. Informasi Orang Tua/Wali
        self.parent_name = page.get_by_role("textbox", name="Parent/Guardian Name")
        self.parent_phone = page.get_by_role("textbox", name="Parent/Guardian Phone")
        self.parent_email = page.get_by_role("textbox", name="Parent/Guardian Email")

        # 3. Kontak Darurat
        self.emergency_name = page.get_by_role("textbox", name="Emergency Contact Name")
        self.emergency_phone = page.get_by_role("textbox", name="Emergency Contact Phone")
        self.relationship = page.get_by_label("Relationship")

        # 4. Latar Belakang Pendidikan
        self.high_school = page.get_by_role("textbox", name="High School Name")
        self.graduation_year = page.get_by_label("Graduation Year")
        self.education_level = page.get_by_label("Previous Education Level")

        # 5. Informasi Akademik
        self.generate_nim_btn = page.get_by_role("button", name="Generate Student ID")
        self.student_id = page.get_by_role("textbox", name="Student ID")
        self.study_program = page.get_by_label("Department")
        self.entry_year = page.get_by_label("Entry Year")
        self.degree = page.get_by_label("Degree")
        self.current_semester = page.get_by_label("Current Semester")
        self.class_type = page.get_by_label("Class Type")
        self.entry_path = page.get_by_label("Entry Path")
        self.status = page.get_by_label("Status")

        # Tombol Submit
        self.submit_btn = page.get_by_role("button", name="save")

    def navigate(self):
        self.master_menu.click()
        self.master_student_menu.click()
    
    def add(self, data):
        self.add_new_student_btn.click()
        
        # Informasi Pribadi
        self.full_name.fill(data["full_name"])
        self.username.fill(data["username"])
        self.email.fill(data["email"])
        self.nisn.fill(data["nisn"])
        self.gender.select_option(data["gender"])
        self.religion.select_option(data["religion"])
        self.date_of_birth.fill(data["date_of_birth"])
        self.place_of_birth.fill(data["place_of_birth"])
        self.phone.fill(data["phone"])
        self.address.fill(data["address"])

        # Orang Tua/Wali
        self.parent_name.fill(data["parent_name"])
        self.parent_phone.fill(data["parent_phone"])
        self.parent_email.fill(data["parent_email"])

        # Kontak Darurat
        self.emergency_name.fill(data["emergency_name"])
        self.emergency_phone.fill(data["emergency_phone"])
        self.relationship.select_option(data["relationship"])

        # Pendidikan
        self.high_school.fill(data["high_school"])
        self.graduation_year.select_option(data["graduation_year"])
        self.education_level.select_option(data["education_level"])

        # Akademik
        self.generate_nim_btn.click()
        
        self.study_program.select_option(data["study_program"])
        self.entry_year.select_option(data["entry_year"])
        self.degree.select_option(data["degree"])
        self.current_semester.select_option(data["current_semester"])
        
        # Optional Fields
        try:
            self.class_type.select_option(data["class_type"])
        except:
            pass

        # Handle Entry Path (mungkin tidak ada asterisk)
        try:
            self.entry_path.select_option(data["entry_path"])
        except:
            pass
            
        self.status.select_option(data["status"])

        # Kirim data
        self.submit_btn.click()

    def details(self, name):
        self.page.get_by_role("row", name=name).get_by_role("button", name="Details").click()

    def verify_details(self, data):
        def check(label, value):
            expect(self.page.locator("div").filter(has_text=label).last).to_contain_text(value)

        # Verifikasi Data
        check("Full Name", data["full_name"])
        check("Username", data["username"])
        check("Email", data["email"])
        check("NISN", data["nisn"])
        check("Gender", data["gender"])
        check("Phone Number", data["phone"])
        check("Religion", data["religion"])
        check("Place of Birth", data["place_of_birth"])
        check("Address", data["address"])

        # Tanggal Lahir
        try:
            date_obj = datetime.strptime(data["date_of_birth"], "%Y-%m-%d")
            display_date = f"{date_obj.day}/{date_obj.month}/{date_obj.year}"
            check("Date of Birth", display_date)
        except Exception:
            check("Date of Birth", data["date_of_birth"])
            
        # Student ID
        expect(self.page.locator("div").filter(has_text="Student ID").last).not_to_be_empty()
        
        # Tutup Modal
        self.page.keyboard.press("Escape")
        self.page.wait_for_timeout(500)

    def delete(self, name):
        self.details(name)
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.delete_btn.click()
        self.page.wait_for_load_state("networkidle")
