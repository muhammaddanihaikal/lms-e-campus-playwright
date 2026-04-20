"""LoginPage — entry point halaman login.

Page Object hanya bertanggung jawab navigasi & buka komponen.
Aksi detail (fill form, submit) ada di LoginForm component.
"""

from config.config import BASE_URL
from pages.base_page import BasePage
from pages.authentication.components.login_form import LoginForm


class LoginPage(BasePage):

    def navigate(self):
        self.page.goto(f"{BASE_URL}/login", timeout=180000)
        self.page.get_by_label("Username *").wait_for(state="visible", timeout=180000)

    # Backward-compat alias
    def open(self):
        self.navigate()

    def login(self, data, expected_url: str = "**/Adminoffice"):
        """Convenience: open form, fill, submit, tunggu redirect.

        data: dict { username, password }
        expected_url: glob URL yang ditunggu setelah submit
        """
        form = LoginForm(self.page)
        form.fill_credentials(data["username"], data["password"])
        form.submit()
        self.page.wait_for_url(expected_url, timeout=60000)
        self.page.wait_for_load_state("networkidle", timeout=60000)
