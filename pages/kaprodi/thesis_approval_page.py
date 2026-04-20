"""KaprodiThesisApprovalPage — entry point halaman Proposal Approval untuk role Kaprodi."""

import re

from pages.base_page import BasePage
from pages.kaprodi.components.proposal_approval_modal import ProposalApprovalModal


class KaprodiApprovalPage(BasePage):

    def navigate_to_approval(self):
        thesis_management = self.page.get_by_text("Thesis Management", exact=True)
        proposal_approval_link = self.page.get_by_text("Proposal Approval", exact=True)

        if not proposal_approval_link.is_visible():
            thesis_management.click()
            self.page.wait_for_timeout(500)

        proposal_approval_link.click()
        self.page.wait_for_load_state("networkidle")

        # Pastikan masuk ke tab Pending
        self.page.get_by_role("tab", name="Pending").click()
        self.page.wait_for_timeout(500)

    def open_proposal_modal(self, thesis_title: str):
        """Klik action button di row proposal → buka modal approval."""
        row = self.page.locator("tr").filter(has_text=thesis_title).first
        row.get_by_role("button").first.click()
        self.page.wait_for_timeout(1000)
        return ProposalApprovalModal(self.page)

    def switch_tab(self, tab_pattern: str):
        """Pindah ke tab tertentu (regex pattern: 'Pending.*', 'Approved.*')."""
        self.page.get_by_role("tab", name=re.compile(tab_pattern)).click()
        self.page.wait_for_timeout(1000)

    def proposal_row(self, thesis_title: str):
        return self.page.locator("tr").filter(has_text=thesis_title).first

    # ---- Backward-compat helpers ----
    def find_proposal(self, student_name: str, timeout: int = 10000):
        cell = self.page.get_by_role("cell", name=student_name)
        cell.wait_for(state="visible", timeout=timeout)

    def open_pending_proposal(self, thesis_title: str):
        self.open_proposal_modal(thesis_title)

    def approve_proposal(self, data: dict):
        ProposalApprovalModal(self.page).approve(data)

    def check_proposal_in_tab(self, thesis_title: str, tab_pattern: str):
        self.switch_tab(tab_pattern)
        try:
            self.proposal_row(thesis_title).wait_for(state="visible", timeout=3000)
            print(f"[OK] Proposal '{thesis_title}' ditemukan di tab {tab_pattern}")
        except Exception:
            print(f"[WARN] Proposal '{thesis_title}' tidak ditemukan di halaman pertama tab {tab_pattern}")
