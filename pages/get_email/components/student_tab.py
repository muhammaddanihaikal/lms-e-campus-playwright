from playwright.sync_api import Page

class StudentTab:
    def __init__(self, page: Page):
        self.page = page

        # verify
        self.email = page.get_by_role("textbox", name="Personal Email Address *")
        self.student_id = page.get_by_role("textbox", name="Student ID (NIM) *")
        self.verify_btn = page.get_by_role("button", name="Verify Student Record")
        self.success_alert = page.get_by_role("tabpanel", name="Student").get_by_role("alert")

        # create account
        self.username = page.get_by_role("textbox", name="Choose Username *")
        self.password = page.get_by_role("textbox", name="Create Password *")
        self.confirm_password = page.get_by_role("textbox", name="Confirm Password *")
        self.create_account_btn = page.get_by_role("button", name="Create Campus Account")
        self.success_alert = page.get_by_text("Registration Successful!Your")

    def verify(self, data):
        self.email.fill(data["email"])
        self.student_id.fill(data["student_id"])
        self.verify_btn.click()
        self.success_alert.wait_for(state="visible")
    
    def create_account(self, data):
        self.username.fill(data["username"])
        self.password.fill(data["password"])
        self.confirm_password.fill(data["confirm_password"])
        self.create_account_btn.click()
        self.success_alert.wait_for(state="visible")