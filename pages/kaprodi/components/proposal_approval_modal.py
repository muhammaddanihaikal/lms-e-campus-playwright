"""ProposalApprovalModal — modal approve proposal thesis untuk Kaprodi."""

from pages.base_page import BasePage


class ProposalApprovalModal(BasePage):

    def click_approve(self):
        self.page.get_by_role("button", name="Approve").click()
        self.page.wait_for_timeout(200)

    def select_advisor(self, advisor_value: str):
        self.page.get_by_label("Choose Advisor **").select_option(advisor_value)
        self.page.wait_for_timeout(100)

    def fill_note(self, note: str):
        self.page.get_by_role("textbox", name="Approval Note (Optional)").fill(note)

    def confirm(self):
        self.page.get_by_role("button", name="Approve Proposal").click()
        self.page.wait_for_load_state("networkidle")

    def approve(self, data: dict):
        """Convenience: jalankan urutan approve sampai konfirmasi."""
        self.click_approve()
        if "advisor" in data:
            self.select_advisor(data["advisor"])
        if "approval_note" in data:
            self.fill_note(data["approval_note"])
        self.confirm()
