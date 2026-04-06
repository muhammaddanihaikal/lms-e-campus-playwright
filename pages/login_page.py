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

    def login(self, data, expected_url: str = "**/Adminoffice"):
        """Login dengan username dan password
        
        Args:
            data: Dictionary dengan username dan password
            expected_url: URL yang ditunggu setelah login (default: **/Adminoffice)
        """
        self.username.fill(data["username"])
        self.password.fill(data["password"])
        # Debug: take screenshot to see current state
        self.page.screenshot(path="debug_login.png")

        # Try multiple strategies to find the login button
        # Strategy 1: Button with text "Login"
        # Strategy 2: Button with text "Masuk"
        # Strategy 3: First submit/login type button
        button = None
        for btn_text in ["Login", "Masuk", "Sign In", "Sign in", "LOGIN"]:
            btn = self.page.get_by_role("button", name=btn_text)
            if btn.is_visible(timeout=5000):
                button = btn
                break

        # If no button found with specific text, try generic selectors
        if button is None:
            # Try to find any submit button
            button = self.page.locator('button[type="submit"]').first
            if not button.is_visible(timeout=5000):
                # Try any button element
                button = self.page.locator('button').first

        button.click()
        self.page.wait_for_url(expected_url, timeout=60000)
        self.page.wait_for_load_state("networkidle", timeout=60000)