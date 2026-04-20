"""Test suite Master Kaprodi: add kaprodi (admin office)."""

import allure
from playwright.sync_api import expect

from utils.faker_helper import generate_kaprodi


@allure.title("TC-10: 🟡 PENDING — Tambah kaprodi baru via Master Kaprodi")
def test_add_kaprodi(master_kaprodi_page):
    # Arrange
    data = generate_kaprodi()

    # Act
    employee_id = master_kaprodi_page.add(data)
    master_kaprodi_page.page.reload()
    master_kaprodi_page.page.wait_for_load_state("networkidle")
    master_kaprodi_page.search(employee_id)

    # Assert
    expect(master_kaprodi_page.table).to_contain_text(employee_id)
