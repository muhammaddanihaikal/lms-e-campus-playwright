from playwright.sync_api import Page
from config.config import BASE_URL

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        # Penanda elemen (locator)
        self.username = page.get_by_role("textbox", name="Username")
        self.password = page.get_by_role("textbox", name="Password")
        self.login_btn = page.get_by_role("button", name="Login")

    def open(self):
        self.page.goto(f"{BASE_URL}/login")

    def login(self, data):
        self.username.fill(data["username"])
        self.password.fill(data["password"])
        self.login_btn.click()
        self.page.wait_for_url("**/Adminoffice", timeout=10000)
        self.page.wait_for_load_state("networkidle")