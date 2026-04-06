from playwright.sync_api import Page


class AddDepartmentModal:
    """Component for Add Department Modal"""

    def __init__(self, page: Page):
        self.page = page

        # Department Information
        self.department_code = page.locator("input[name='code']")
        self.department_name = page.locator("input[name='name']")
        self.description = page.locator("textarea[name='description']")
        self.faculty = page.locator("select[name='faculty_id']")
        self.degree_level = page.locator("select[name='degree_level']")
        self.degree_title = page.locator("select[name='degree_title']")
        self.head_of_department = page.locator("input[name='head_of_department']")
        self.email = page.locator("input[name='email']")
        self.phone = page.locator("input[name='phone']")
        self.address = page.locator("textarea[name='address']")
        self.established_year = page.locator("select[name='established_year']")
        self.accreditation = page.locator("select[name='accreditation']")
        self.status = page.locator("select[name='status']")

        # Submit button
        self.save_btn = page.get_by_role("button", name="Save")

    def fill_form(self, data: dict) -> str:
        self.department_code.fill(data["department_code"])
        self.department_name.fill(data["department_name"])
        self.description.fill(data["description"])
        self.faculty.select_option(data["faculty"])
        self.degree_level.select_option(data["degree_level"])
        self.degree_title.select_option(data["degree_title"])
        self.head_of_department.fill(data["head_of_department"])
        self.email.fill(data["email"])
        self.phone.fill(data["phone"])
        self.address.fill(data["address"])
        self.established_year.select_option(data["established_year"])
        self.accreditation.select_option(data["accreditation"])
        self.status.select_option(data["status"])

        return data["department_code"]

    def submit(self):
        self.save_btn.click()
