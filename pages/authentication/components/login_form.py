"""LoginForm component — fill credentials & submit."""

from pages.base_page import BasePage


class LoginForm(BasePage):

    def fill_credentials(self, username: str, password: str):
        self.page.get_by_label("Username *").fill(username)
        self.page.get_by_label("Password *").fill(password)

    def submit(self):
        for btn_text in ["Log In", "Login", "Masuk", "Sign In", "Sign in", "LOGIN"]:
            btn = self.page.get_by_role("button", name=btn_text)
            if btn.is_visible(timeout=5000):
                btn.click()
                return
        # Fallback ke submit button apapun
        self.page.locator('button[type="submit"]').first.click()
