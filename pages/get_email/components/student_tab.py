from playwright.sync_api import Page

class StudentTab:
    def __init__(self, page: Page):
        self.page = page

        # tabpanel
        self.panel = page.get_by_role("tabpanel", name="Student")

        # verify
        self.email = self.panel.get_by_role("textbox", name="Personal Email Address *")
        self.student_id = self.panel.get_by_role("textbox", name="Student ID (NIM) *")
        self.verify_btn = self.panel.get_by_role("button", name="Verify Student Record")
        self.verify_success_alert = self.panel.get_by_role("alert").filter(has_text="Student Verification")

        # create account
        self.username = self.panel.get_by_role("textbox", name="Choose Username *")
        self.password = self.panel.get_by_role("textbox", name="Create Password *")
        self.confirm_password = self.panel.get_by_role("textbox", name="Confirm Password *")
        self.create_account_btn = self.panel.get_by_role("button", name="Create Campus Account")
        self.create_success_alert = self.panel.get_by_text("Registration Successful!")

    def verify(self, data):
        self.email.fill(data["email"])
        self.student_id.fill(data["student_id"])
        self.verify_btn.click()
        self.verify_success_alert.wait_for(state="visible")
    
    def create_account(self, data):
        self.username.fill(data["username"])
        self.password.fill(data["password"])
        self.confirm_password.fill(data["confirm_password"])
        self.create_account_btn.click()
        self.create_success_alert.wait_for(state="visible")