"""E2E Test: Kaprodi complete thesis approval journey.

Flow: Login → navigate → check pending proposals → approve jika ada (idempotent).
"""

import re

import allure
import pytest
from playwright.sync_api import expect

from utils.faker_helper import generate_thesis_proposal


@allure.title("TC-23: 🟡 PENDING — Kaprodi E2E: navigate & approve pending proposals")
def test_kaprodi_approval_journey(kaprodi_e2e_actors, login_credentials):
    # Arrange
    actors = kaprodi_e2e_actors
    page = actors["login"].page
    kaprodi_cred = login_credentials["kaprodi"]
    student_cred = login_credentials["student"]
    student_name = student_cred["username"]

    # Act — Login
    actors["login"].open()
    actors["login"].login(kaprodi_cred, expected_url="**/Adminkaprodi*")

    # Navigate ke Proposal Approval
    approval = actors["approval"]
    approval.navigate_to_approval()
    page.wait_for_load_state("networkidle")

    # Check pending proposals di tab
    page.get_by_role("tab", name=re.compile(r"Pending.*")).click()
    page.wait_for_timeout(1000)

    # Cari proposal dengan nama student
    student_proposal_title = f"Tesis Sistem Informasi {student_name}"
    row = approval.proposal_row(student_proposal_title)
    if not row.is_visible():
        pytest.skip(f"Tidak ada proposal pending dari {student_name} — sudah di-approve atau belum submit")
    else:
        # Ada proposal → approve
        modal = approval.open_proposal_modal(student_proposal_title)
        modal.approve({"note": "Approved via E2E test"})
        page.wait_for_timeout(2000)

        # Assert — verify pindah ke tab Approved
        approval.switch_tab(r"Approved.*")
        expect(approval.proposal_row(student_proposal_title)).to_be_visible()

    # Logout
    actors["navbar"].logout()
    expect(page).to_have_url("**/login*")
