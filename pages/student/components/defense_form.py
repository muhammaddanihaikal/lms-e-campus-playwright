"""DefenseForm — modal Submit Defense Request (upload ZIP)."""

import os

from pages.base_page import BasePage


class DefenseForm(BasePage):

    def upload_zip(self, zip_path: str):
        if not os.path.exists(zip_path):
            raise FileNotFoundError(f"File zip defense tidak ditemukan: {zip_path}")
        self.page.locator('input[type="file"]').first.set_input_files(zip_path)
        self.page.wait_for_timeout(1000)

    def submit(self):
        self.page.get_by_role("button", name="Submit Request").click()
        self.page.wait_for_load_state("networkidle")
