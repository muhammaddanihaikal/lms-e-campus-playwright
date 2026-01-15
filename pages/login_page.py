from playwright.sync_api import Page
from config.config import BASE_URL

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_label("Username *")
        self.password = page.get_by_label("Password *")
        self.login_btn = page.get_by_role("button", name="Login")

    def open(self):
        print(f"Navigating to {BASE_URL}/login ...")
        # Gunakan timeout yang lebih lama untuk navigasi awal (3 menit)
        self.page.goto(f"{BASE_URL}/login", timeout=180000)
        print("Navigation finished. Waiting for username field...")
        # Tunggu sampai muncul dengan timeout 3 menit
        self.username.wait_for(state="visible", timeout=180000)
        print("Username field is visible.")

    def login(self, data):
        self.username.fill(data["username"])
        self.password.fill(data["password"])
        self.login_btn.click()
        self.page.wait_for_url("**/Adminoffice")
        self.page.wait_for_load_state("networkidle")