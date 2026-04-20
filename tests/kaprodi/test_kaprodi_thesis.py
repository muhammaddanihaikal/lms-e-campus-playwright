"""Test suite Kaprodi: approve proposal & approve defense request."""

import re

import allure
import pytest
from playwright.sync_api import expect


@allure.title("TC-18: 🟡 PENDING — Approve proposal thesis di tab Pending")
def test_approve_proposal(kaprodi_approval_page, valid_approval_data, valid_proposal_data_for_kaprodi):
    # Arrange
    page = kaprodi_approval_page.page
    title = valid_proposal_data_for_kaprodi["thesis_title"]

    # Act
    kaprodi_approval_page.navigate_to_approval()

    if not kaprodi_approval_page.proposal_row(title).is_visible():
        pytest.skip(f"Proposal '{title}' tidak ada di tab Pending — sudah di-approve atau belum disubmit.")

    modal = kaprodi_approval_page.open_proposal_modal(title)
    modal.approve(valid_approval_data)

    # Assert — pindah ke tab Approved & proposal muncul
    kaprodi_approval_page.switch_tab(r"Approved.*")
    expect(kaprodi_approval_page.proposal_row(title)).to_be_visible()


@allure.title("TC-21: 🟡 PENDING — Approve defense request di tab Submitted")
def test_approve_defense_request(kaprodi_defense_page, login_credentials):
    # Arrange
    page = kaprodi_defense_page.page
    student_username = login_credentials["student"]["username"]

    # Act
    kaprodi_defense_page.navigate_to_defense_documents()
    kaprodi_defense_page.switch_tab(r"Submitted.*")

    row = page.locator("tr").filter(has_text=re.compile(student_username, re.IGNORECASE)).first
    if not row.is_visible():
        pytest.skip(f"Defense request student '{student_username}' tidak ada di Submitted.")

    modal = kaprodi_defense_page.open_review_modal(student_username)
    modal.accept()

    # Assert — pindah ke tab Approved
    kaprodi_defense_page.switch_tab(r"Approved.*")
    expect(
        page.locator("tr").filter(has_text=re.compile(student_username, re.IGNORECASE)).first
    ).to_be_visible()


@pytest.fixture
def valid_proposal_data_for_kaprodi(valid_approval_data, login_credentials):
    """Re-use proposal title pattern dari thesis flow agar lookup di kaprodi konsisten."""
    student_username = login_credentials["student"]["username"]
    return {
        "thesis_title": f"Tesis Sistem Informasi {student_username}",
    }
