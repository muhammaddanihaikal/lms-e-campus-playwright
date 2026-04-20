"""KaprodiDefenseDocumentsPage — entry point halaman Defense Documents untuk role Kaprodi."""

import re

from pages.base_page import BasePage
from pages.kaprodi.components.defense_review_modal import DefenseReviewModal


class KaprodiDefenseDocumentsPage(BasePage):

    def navigate_to_defense_documents(self):
        thesis_management = self.page.get_by_text("Thesis Management", exact=True)
        defense_link = self.page.get_by_text("Thesis Documents", exact=True)

        if not defense_link.is_visible():
            thesis_management.click()
            self.page.wait_for_timeout(500)

        defense_link.click()
        self.page.wait_for_load_state("networkidle")

        # Default tab Submitted
        self.page.get_by_role("tab", name="Submitted").click()
        self.page.wait_for_timeout(500)

    def switch_tab(self, tab_pattern: str):
        self.page.get_by_role("tab", name=re.compile(tab_pattern)).click()
        self.page.wait_for_timeout(1000)

    def open_review_modal(self, student_name: str):
        row = self.page.locator("tr").filter(has_text=re.compile(student_name, re.IGNORECASE)).first
        row.get_by_role("button", name="Review").first.click()
        self.page.wait_for_timeout(1000)
        return DefenseReviewModal(self.page)

    # ---- Backward-compat helpers ----
    def check_defense_in_tab(self, student_name: str, tab_pattern: str):
        self.switch_tab(tab_pattern)
        row = self.page.locator("tr").filter(has_text=re.compile(student_name, re.IGNORECASE)).first
        try:
            row.wait_for(state="visible", timeout=3000)
            print(f"[OK] Defense '{student_name}' ditemukan di tab {tab_pattern}")
        except Exception:
            print(f"[WARN] Defense '{student_name}' tidak ditemukan di halaman pertama tab {tab_pattern}")

    def accept_defense_request(self, student_name: str):
        DefenseReviewModal(self.page).open_and_accept(self.page, student_name)
