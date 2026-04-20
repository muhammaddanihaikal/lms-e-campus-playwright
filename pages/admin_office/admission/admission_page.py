"""AdmissionPage & ApprovalPage — entry point halaman pendaftaran admission."""

from config.config import BASE_URL
from pages.base_page import BasePage
from pages.admin_office.admission.components.admission_form import AdmissionForm


class AdmissionPage(BasePage):

    def navigate(self):
        self.page.goto(f"{BASE_URL}/login")
        self.page.wait_for_load_state("networkidle")
        self.page.get_by_role("link", name="Admission").click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)

    # Backward-compat
    def open(self):
        self.navigate()

    def open_admission_form(self):
        return AdmissionForm(self.page)

    def submit(self, data):
        """Backward-compat: bantuan all-in-one."""
        form = self.open_admission_form()
        form.fill(data)
        form.submit()


class ApprovalPage(BasePage):
    """Pending Admissions section di dashboard admin office."""

    def navigate(self):
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)

    def open(self):
        self.navigate()

    def refresh(self):
        self.page.reload()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)

    def has_pending_admissions(self) -> bool:
        return self.page.get_by_text("No pending admissions").count() == 0

    def approve_admission(self, full_name: str) -> bool:
        student_element = self.page.get_by_text(full_name, exact=False)
        if student_element.count() > 0:
            approve_btn = student_element.locator("button", has_text="Approve")
            if approve_btn.count() > 0:
                approve_btn.first.click()
                self.page.wait_for_timeout(2000)
                return True
        return False

    def reject_admission(self, full_name: str) -> bool:
        student_element = self.page.get_by_text(full_name, exact=False)
        if student_element.count() > 0:
            reject_btn = student_element.locator("button", has_text="Reject")
            if reject_btn.count() > 0:
                reject_btn.first.click()
                self.page.wait_for_timeout(2000)
                return True
        return False
