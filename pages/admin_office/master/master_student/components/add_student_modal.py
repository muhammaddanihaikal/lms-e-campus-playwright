from playwright.sync_api import Page

class AddStudentModal:
    def __init__(self, page: Page):
        self.page = page
        
        # Informasi Pribadi
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

        # Informasi Orang Tua/Wali
        self.parent_name = page.get_by_role("textbox", name="Parent/Guardian Name")
        self.parent_phone = page.get_by_role("textbox", name="Parent/Guardian Phone")
        self.parent_email = page.get_by_role("textbox", name="Parent/Guardian Email")

        # Kontak Darurat
        self.emergency_name = page.get_by_role("textbox", name="Emergency Contact Name")
        self.emergency_phone = page.get_by_role("textbox", name="Emergency Contact Phone")
        self.relationship = page.get_by_label("Relationship")

        # Latar Belakang Pendidikan
        self.high_school = page.get_by_role("textbox", name="High School Name")
        self.graduation_year = page.get_by_label("Graduation Year")
        self.education_level = page.get_by_label("Previous Education Level")

        # Informasi Akademik
        self.generate_btn = page.get_by_role("button", name="Generate Student ID")
        self.student_id = page.get_by_role("textbox", name="Student ID (NIM)")
        self.study_program = page.get_by_label("Department")
        self.entry_year = page.get_by_label("Entry Year")
        self.degree = page.get_by_label("Degree")
        self.current_semester = page.get_by_label("Current Semester")
        self.class_type = page.get_by_label("Class Type")
        self.entry_path = page.get_by_label("Entry Path")
        self.status = page.get_by_label("Status")

        # Tombol Submit
        self.submit_btn = page.get_by_role("button", name="save")

    def fill_form(self, data):
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
        self.generate_btn.click()
        
        # Ambil student id
        student_id = self.student_id.input_value()
        
        self.study_program.select_option(data["study_program"])
        self.entry_year.select_option(data["entry_year"])
        self.degree.select_option(data["degree"])
        self.current_semester.select_option(data["current_semester"])
        self.class_type.select_option(data["class_type"])
        self.entry_path.select_option(data["entry_path"])
        self.status.select_option(data["status"])
        
        return student_id

    def submit(self):
        self.submit_btn.click()
