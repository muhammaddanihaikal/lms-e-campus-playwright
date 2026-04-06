from playwright.sync_api import Page


class EditFacultyModal:
    """Component for Edit Faculty Modal"""

    def __init__(self, page: Page):
        self.page = page

        # Faculty Information
        self.faculty_code = page.locator("input[name='code']")
        self.faculty_name = page.locator("input[name='name']")
        self.dean_name = page.locator("input[name='dean_name']")
        self.vice_dean_name = page.locator("input[name='vice_dean_name']")
        self.email = page.locator("input[name='email']")
        self.phone = page.locator("input[name='phone']")
        self.address = page.locator("textarea[name='address']")
        self.status = page.locator("select[name='status']")
        self.established_year = page.locator("select[name='established_year']")
        self.accreditation = page.locator("select[name='accreditation']")
        self.description = page.locator("textarea[name='description']")

        # Submit button
        self.save_btn = page.get_by_role("button", name="Update")

    def fill_form(self, data: dict):
        # Skip faculty_code karena readonly di edit mode
        self.faculty_name.fill(data["faculty_name"])
        self.dean_name.fill(data["dean_name"])
        self.vice_dean_name.fill(data["vice_dean_name"])
        self.email.fill(data["email"])
        self.phone.fill(data["phone"])
        self.address.fill(data["address"])
        self.status.select_option(data["status"])
        self.established_year.select_option(data["established_year"])
        self.accreditation.select_option(data["accreditation"])
        self.description.fill(data["description"])

    def submit(self):
        self.save_btn.click()
