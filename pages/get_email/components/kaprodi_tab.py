from playwright.sync_api import Page

class KaprodiTab:
    def __init__(self, page: Page):
        self.page = page

        # tabpanel
        self.panel = page.get_by_role("tabpanel", name="Kaprodi")

        # verify
        self.email_field = self.panel.get_by_role("textbox", name="Personal Email Address *")
        self.employee_id_field = self.panel.get_by_role("textbox", name="Kaprodi/Employee ID *")
        self.verify_btn = self.panel.get_by_role("button", name="Verify Kaprodi Record")
        
        # create account
        self.username_field = self.panel.get_by_role("textbox", name="Choose Username *")
        self.password_field = self.panel.get_by_role("textbox", name="Create Password *")
        self.confirm_password_field = self.panel.get_by_role("textbox", name="Confirm Password *")
        self.create_account_btn = self.panel.get_by_role("button", name="Create Campus Account")
        self.create_success_alert = self.panel.get_by_text("Registration Successful!")

    def verify(self, data):
        self.email_field.fill(data["email"])
        self.employee_id_field.fill(data["employee_id"])
        self.verify_btn.click()
        # Wait for Step 2 or username field to appear
        self.username_field.wait_for(state="visible", timeout=10000)
    
    def create_account(self, data):
        self.username_field.fill(data["username"])
        self.password_field.fill(data["password"])
        self.confirm_password_field.fill(data["confirm_password"])
        self.create_account_btn.click()
        self.create_success_alert.wait_for(state="visible")