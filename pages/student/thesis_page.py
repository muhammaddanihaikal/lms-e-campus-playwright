"""StudentThesisPage — entry point halaman Thesis untuk role Student.

Page hanya untuk navigasi & buka modal/sub-page.
Aksi detail (fill form, upload, submit) ada di components/.
"""

from pages.base_page import BasePage
from pages.student.components.proposal_form import ProposalForm
from pages.student.components.defense_form import DefenseForm


class StudentThesisPage(BasePage):

    def navigate_to_thesis(self):
        """Klik menu accordion Thesis di sidebar."""
        self.page.get_by_role("button", name="Thesis Thesis").click()
        self.page.wait_for_timeout(200)

    def navigate_to_defense(self):
        """Buka submenu Defense (asumsi accordion Thesis sudah terbuka)."""
        self.page.get_by_text("Defense").first.click()
        self.page.wait_for_load_state("networkidle")

    def open_proposal_form(self):
        """Klik Start Thesis Proposal lalu Create Thesis & Submit."""
        self.page.get_by_role("button", name="Start Thesis Proposal").click()
        self.page.wait_for_timeout(200)
        self.page.get_by_role("button", name="Create Thesis & Submit").click()
        self.page.wait_for_timeout(500)
        return ProposalForm(self.page)

    def open_defense_form(self):
        """Buka modal Submit Defense Request."""
        self.navigate_to_thesis()
        self.navigate_to_defense()
        self.page.get_by_role("button", name="Submit Defense Request").click()
        self.page.wait_for_timeout(500)
        return DefenseForm(self.page)

    # ---- Backward-compat convenience helpers ----
    # Dipakai oleh test e2e existing supaya tidak break.

    def start_proposal(self):
        self.page.get_by_role("button", name="Start Thesis Proposal").click()
        self.page.wait_for_timeout(200)

    def create_thesis(self):
        self.page.get_by_role("button", name="Create Thesis & Submit").click()
        self.page.wait_for_timeout(500)

    def fill_proposal_form(self, data: dict):
        ProposalForm(self.page).fill(data)

    def upload_proposal(self, file_path: str):
        ProposalForm(self.page).upload(file_path)

    def submit_proposal(self):
        ProposalForm(self.page).submit()

    def submit_defense_request(self, zip_path: str):
        form = self.open_defense_form()
        form.upload_zip(zip_path)
        form.submit()
