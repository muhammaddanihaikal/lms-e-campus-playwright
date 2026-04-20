"""ResearchApprovalModal — modal approve fase Research untuk Dosen."""

from pages.base_page import BasePage


class ResearchApprovalModal(BasePage):

    def open_research_tab(self):
        research_tab = self.page.get_by_role("heading", name="Research")
        if research_tab.is_visible():
            research_tab.click()
        else:
            self.page.get_by_text("Research").first.click()
        self.page.wait_for_timeout(500)

    def click_approve(self) -> bool:
        """Klik tombol Approve. Return False jika tombol tidak muncul."""
        approve_btn = self.page.get_by_role("button", name="Approve")
        if not approve_btn.is_visible(timeout=5000):
            return False
        approve_btn.click()
        self.page.wait_for_timeout(500)
        return True

    def fill_note(self, note: str):
        try:
            self.page.get_by_role("textbox", name="Approval Note (Optional)").fill(note)
        except Exception:
            self.page.get_by_placeholder("Approval Note").fill(note)

    def confirm(self):
        try:
            self.page.get_by_role("button", name="Approve & Continue").click()
        except Exception:
            self.page.get_by_role("button", name="Approve Result").click()
        self.page.wait_for_load_state("networkidle")

    def approve_research(self, note: str = "test") -> bool:
        """Convenience: buka tab Research → Approve → fill → Confirm.

        Return True jika berhasil, False jika sudah pernah di-approve.
        """
        self.open_research_tab()
        if not self.click_approve():
            print("[INFO] Tombol Approve tidak ada — research sudah di-approve.")
            return False
        self.fill_note(note)
        self.confirm()
        return True
