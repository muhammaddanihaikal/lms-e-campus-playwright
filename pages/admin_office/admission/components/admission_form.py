"""AdmissionForm — komponen form pendaftaran admission (multi-section)."""

from pages.base_page import BasePage


class AdmissionForm(BasePage):

    def fill_personal(self, data: dict):
        self.page.locator('input[name="name"]').fill(data["full_name"])
        self.page.locator('input[name="nisn"]').fill(data["nisn"])
        self.page.locator('input[name="birthPlace"]').fill(data["place_of_birth"])
        self.page.locator('input[name="birthDate"]').fill(data["date_of_birth"])
        self.page.locator('select[name="gender"]').select_option(data["gender"])
        self.page.locator('select[name="religion"]').select_option(data["religion"])
        self.page.locator('textarea[name="address"]').fill(data["address"])
        self.page.locator('input[name="email"]').fill(data["email"])
        self.page.locator('input[name="phone"]').fill(data["phone"])

    def fill_parent(self, data: dict):
        self.page.locator('input[name="parentName"]').fill(data["parent_name"])
        self.page.locator('input[name="parentPhone"]').fill(data["parent_phone"])
        self.page.locator('input[name="parentEmail"]').fill(data["parent_email"])

    def fill_emergency(self, data: dict):
        self.page.locator('input[name="emergencyContactName"]').fill(data["emergency_name"])
        self.page.locator('input[name="emergencyContactPhone"]').fill(data["emergency_phone"])
        self.page.locator('select[name="emergencyContactRelation"]').select_option(data["relationship"])

    def fill_education(self, data: dict):
        self.page.locator('input[name="highSchoolName"]').fill(data["high_school"])
        self.page.locator('select[name="graduationYear"]').select_option(data["graduation_year"])
        self.page.locator('select[name="previousEducationLevel"]').select_option(data["education_level"])

    def fill_program(self, data: dict):
        self.page.locator('select[name="studyProgram"]').select_option(data["study_program"])
        self.page.locator('select[name="classType"]').select_option(data["class_type"])
        self.page.locator('select[name="entryPath"]').select_option(data["entry_path"])

    def upload_documents(self, data: dict):
        self.page.locator('input[name="report"]').set_input_files(data["academic_transcript"])
        self.page.locator('input[name="certificate"]').set_input_files(data["diploma"])
        self.page.locator('input[name="idCard"]').set_input_files(data["national_id"])
        self.page.locator('input[name="familyCard"]').set_input_files(data["family_card"])

    def submit(self):
        self.page.get_by_role("button", name="Submit").click()
        self.page.wait_for_timeout(3000)

    def fill(self, data: dict):
        """Convenience: isi seluruh section secara berurutan."""
        self.fill_personal(data)
        self.fill_parent(data)
        self.fill_emergency(data)
        self.fill_education(data)
        self.fill_program(data)
        self.upload_documents(data)
