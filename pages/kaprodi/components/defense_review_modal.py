"""DefenseReviewModal — modal review & accept defense request untuk Kaprodi."""

import re

from pages.base_page import BasePage


class DefenseReviewModal(BasePage):

    def accept(self):
        self.page.get_by_role("button", name="Accept Defense Request").click()
        self.page.wait_for_load_state("networkidle")

    def open_and_accept(self, page, student_name: str):
        """Backward-compat: buka modal lewat row + langsung accept."""
        row = page.locator("tr").filter(has_text=re.compile(student_name, re.IGNORECASE)).first
        row.get_by_role("button", name="Review").first.click()
        page.wait_for_timeout(1000)
        self.accept()
