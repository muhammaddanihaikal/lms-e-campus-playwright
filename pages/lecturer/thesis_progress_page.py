"""LecturerThesisProgressPage — entry point halaman Student Thesis Progress untuk role Dosen."""

import re

from pages.base_page import BasePage
from pages.lecturer.components.research_approval_modal import ResearchApprovalModal


class LecturerThesisProgressPage(BasePage):

    def navigate_to_progress(self):
        try:
            self.page.get_by_role("button", name="Thesis").click()
        except Exception:
            pass  # accordion mungkin sudah expanded
        self.page.wait_for_timeout(500)

        self.page.get_by_role("link", name="Student Thesis Progress").click()
        self.page.wait_for_load_state("networkidle")

    def open_student_progress(self, student_name: str):
        row = self.page.locator("tr").filter(has_text=re.compile(student_name, re.IGNORECASE)).first
        try:
            row.wait_for(state="visible", timeout=5000)
        except Exception:
            print(f"[WARN] Student '{student_name}' mungkin di halaman lain.")
        row.get_by_label("View").first.click()
        self.page.wait_for_load_state("networkidle")
        return ResearchApprovalModal(self.page)

    # ---- Backward-compat ----
    def approve_research_phase(self, notes: str = "test"):
        ResearchApprovalModal(self.page).approve_research(notes)
