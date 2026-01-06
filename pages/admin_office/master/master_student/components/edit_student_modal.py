from playwright.sync_api import Page

class EditStudentModal:
    def __init__(self, page: Page):
        self.page = page
        
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
        # Note: In edit mode, Generate NIM and ID might be read-only or different, 
        # but we'll include them for now based on the add form.
        self.student_id = page.get_by_role("textbox", name="Student ID")
        self.study_program = page.get_by_label("Department")
        self.entry_year = page.get_by_label("Entry Year")
        self.degree = page.get_by_label("Degree")
        self.current_semester = page.get_by_label("Current Semester")
        self.class_type = page.get_by_label("Class Type")
        self.entry_path = page.get_by_label("Entry Path")
        self.status = page.get_by_label("Status")

        # Tombol Submit (Assume it uses "save" name like Add modal)
        self.submit_btn = page.get_by_role("button", name="save")

    def fill_form(self, data):
        # Update fields with provided data if they exist in the dictionary
        
        # 1. Informasi Pribadi
        if "full_name" in data: self.full_name.fill(data["full_name"])
        if "username" in data: self.username.fill(data["username"])
        if "email" in data: self.email.fill(data["email"])
        if "nisn" in data: self.nisn.fill(data["nisn"])
        if "gender" in data: self.gender.select_option(data["gender"])
        if "religion" in data: self.religion.select_option(data["religion"])
        if "date_of_birth" in data: self.date_of_birth.fill(data["date_of_birth"])
        if "place_of_birth" in data: self.place_of_birth.fill(data["place_of_birth"])
        if "phone" in data: self.phone.fill(data["phone"])
        if "address" in data: self.address.fill(data["address"])

        # 2. Informasi Orang Tua/Wali
        if "parent_name" in data: self.parent_name.fill(data["parent_name"])
        if "parent_phone" in data: self.parent_phone.fill(data["parent_phone"])
        if "parent_email" in data: self.parent_email.fill(data["parent_email"])

        # 3. Kontak Darurat
        if "emergency_name" in data: self.emergency_name.fill(data["emergency_name"])
        if "emergency_phone" in data: self.emergency_phone.fill(data["emergency_phone"])
        if "relationship" in data: self.relationship.select_option(data["relationship"])

        # 4. Latar Belakang Pendidikan
        if "high_school" in data: self.high_school.fill(data["high_school"])
        if "graduation_year" in data: self.graduation_year.select_option(data["graduation_year"])
        if "education_level" in data: self.education_level.select_option(data["education_level"])

        # 5. Informasi Akademik
        if "study_program" in data: self.study_program.select_option(data["study_program"])
        if "entry_year" in data: self.entry_year.select_option(data["entry_year"])
        if "degree" in data: self.degree.select_option(data["degree"])
        if "current_semester" in data: self.current_semester.select_option(data["current_semester"])
        if "class_type" in data: self.class_type.select_option(data["class_type"])
        if "entry_path" in data: self.entry_path.select_option(data["entry_path"])
        if "status" in data: self.status.select_option(data["status"])

    def submit(self):
        self.submit_btn.click()
