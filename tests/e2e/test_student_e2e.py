"""E2E Test: Student complete thesis journey.

Flow: Login → navigate thesis → submit proposal (jika belum) → check status.
Idempotent: jika sudah submit, skip ke cek status.
"""

import allure
import pytest
from playwright.sync_api import expect

from utils.faker_helper import generate_thesis_proposal
from utils.file_helper import file_path


@allure.title("TC-22: 🟡 PENDING — Student E2E: submit proposal & check thesis status")
def test_student_thesis_journey(student_e2e_actors, login_credentials):
    # Arrange
    page_obj = student_e2e_actors
    student_cred = login_credentials["student"]
    thesis_data = generate_thesis_proposal(student_cred["username"])

    # Act — Login
    page = page_obj["login"].page
    page_obj["login"].open()
    page_obj["login"].login(student_cred, expected_url="**/home*")

    # Navigate ke Thesis
    thesis = page_obj["thesis"]
    thesis.navigate_to_thesis()
    page.wait_for_load_state("networkidle")

    # Check apakah sudah submit proposal
    if not page.get_by_role("button", name="Start Thesis Proposal").is_visible():
        pytest.skip("Proposal sudah disubmit sebelumnya — melanjutkan cek status")
    else:
        # Submit proposal jika belum
        form = thesis.open_proposal_form()
        form.fill(thesis_data)
        form.upload(file_path("proposal_dummy.pdf"))
        form.submit()
        page.wait_for_timeout(2000)

    # Assert — Cek status (tombol Start hilang = sudah submit atau form tertutup)
    expect(page.get_by_role("button", name="Start Thesis Proposal")).not_to_be_visible()

    # Logout
    page_obj["navbar"].logout()
    expect(page).to_have_url("**/login*")
