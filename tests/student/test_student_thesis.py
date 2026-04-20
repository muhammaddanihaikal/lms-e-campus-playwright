"""Test suite Student Thesis: submit proposal & defense request.

Test ini idempotent — jika student sudah submit, akan di-skip otomatis
via deteksi tombol Start Thesis Proposal.
"""

import allure
import pytest
from playwright.sync_api import expect

from utils.file_helper import file_path


@allure.title("TC-17: 🟡 PENDING — Submit proposal thesis sebagai student")
def test_submit_proposal(student_thesis_page, valid_proposal_data):
    # Arrange
    page = student_thesis_page.page

    # Act
    student_thesis_page.navigate_to_thesis()

    if not page.get_by_role("button", name="Start Thesis Proposal").is_visible():
        pytest.skip("Student sudah pernah submit proposal — tidak ada tombol Start.")

    form = student_thesis_page.open_proposal_form()
    form.fill(valid_proposal_data)
    form.upload(file_path("proposal_dummy.pdf"))
    form.submit()

    # Assert — dialog/toast sukses muncul atau tombol Start hilang
    expect(page.get_by_role("button", name="Start Thesis Proposal")).not_to_be_visible()


@allure.title("TC-20: 🟡 PENDING — Submit defense request dengan file ZIP")
def test_submit_defense_request(student_thesis_page):
    # Arrange
    page = student_thesis_page.page

    # Act
    student_thesis_page.navigate_to_thesis()
    if not page.get_by_text("Defense").first.is_visible():
        pytest.skip("Menu Defense belum unlock (proposal belum approved).")

    student_thesis_page.navigate_to_defense()
    if not page.get_by_role("button", name="Submit Defense Request").is_visible():
        pytest.skip("Defense request sudah pernah disubmit.")

    form = student_thesis_page.open_defense_form()
    form.upload_zip(file_path("defense_dummy.zip"))
    form.submit()

    # Assert
    expect(page.get_by_role("button", name="Submit Defense Request")).not_to_be_visible()
