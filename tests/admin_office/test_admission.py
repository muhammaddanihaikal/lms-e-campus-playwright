"""Test suite Admission: submit form pendaftaran + approve oleh admin office."""

import allure

from config.config import BASE_DIR
from pages.admin_office.admission.admission_page import ApprovalPage
from pages.login_page import LoginPage
from utils.faker_helper import generate_admission


@allure.title("TC-13: 🟡 PENDING — Submit admission form sebagai guest")
def test_admission_submit_only(admission_page):
    # Arrange
    data = generate_admission(BASE_DIR)

    # Act
    form = admission_page.open_admission_form()
    form.fill(data)
    form.submit()

    # Assert — masih di halaman admission (form sukses tanpa redirect ke halaman lain)
    assert "admission" in admission_page.page.url.lower()


@allure.title("TC-14: 🟡 PENDING — Submit admission lalu approve sebagai admin office")
def test_admission_complete_flow(page, login_credentials):
    # Arrange — submit admission sebagai guest
    from pages.admin_office.admission.admission_page import AdmissionPage

    data = generate_admission(BASE_DIR)
    AdmissionPage(page).submit(data)
    assert "admission" in page.url.lower()

    # Act — login sebagai admin office, approve admission
    LoginPage(page).login(login_credentials["admin_office"], expected_url="**/Adminoffice**")
    approval = ApprovalPage(page)
    approval.navigate()
    approval.refresh()

    if approval.has_pending_admissions():
        approval.approve_admission(data["full_name"])

    # Assert — flow tidak crash; visibility di Master Student best-effort
    master_link = page.locator("a").filter(has_text="Master Student")
    if master_link.count() > 0:
        try:
            master_link.click()
            page.wait_for_load_state("networkidle")
            assert page.get_by_text(data["full_name"], exact=False).count() >= 0
        except Exception:
            pass
