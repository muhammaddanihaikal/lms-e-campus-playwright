from playwright.sync_api import Page

class AddLecturerModal:
    def __init__(self, page: Page):
        self.page = page
        
        # User information
        self.lecturer_name = page.get_by_role("textbox", name="Lecturer Name")
        self.email = page.get_by_role("textbox", name="Email")
        self.phone_number = page.get_by_role("textbox", name="Phone Number")
        self.employee_id = page.get_by_placeholder("Enter employee ID or generate one")
        self.generate_btn = page.get_by_role("button", name="Generate")
        self.entry_year = page.get_by_label("Entry Year")
        self.gender = page.get_by_label("Gender")
        self.religion = page.get_by_label("Religion")
        self.date_of_birth = page.get_by_role("textbox", name="Date of Birth")
        self.place_of_birth = page.get_by_role("textbox", name="Place of Birth")
        self.status = page.get_by_label("Status")
        
        # Academic information
        self.faculty = page.get_by_label("Faculty")
        self.department = page.get_by_label("Department")
        
        # buttons
        self.submit_btn = page.get_by_role("button", name="Save")

    def fill_form(self, data):
        self.lecturer_name.fill(data["lecturer_name"])
        self.email.fill(data["email"])
        self.phone_number.fill(data["phone_number"])

        self.generate_btn.click()
        employee_id = self.employee_id.input_value()

        # Fill Entry Year only if visible
        if self.entry_year.is_visible(timeout=500):
            self.entry_year.fill(data["entry_year"])

        self.gender.select_option(data["gender"])
        self.religion.select_option(data["religion"])
        self.date_of_birth.fill(data["date_of_birth"])
        self.place_of_birth.fill(data["place_of_birth"])
        self.status.select_option("Active")

        self.faculty.select_option(label=data["faculty"])
        self.department.wait_for(state="visible")
        self.department.select_option(label=data["department"])
        
        return employee_id

    def submit(self):
        self.submit_btn.click()
