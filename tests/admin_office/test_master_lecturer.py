"""Test suite Master Lecturer: add lecturer (admin office)."""

import allure
from playwright.sync_api import expect

from utils.faker_helper import generate_lecturer


@allure.title("TC-11: 🟡 PENDING — Tambah lecturer baru via Master Lecturer")
def test_add_lecturer(master_lecturer_page):
    # Arrange
    data = generate_lecturer()

    # Act
    employee_id = master_lecturer_page.add(data)
    master_lecturer_page.search(employee_id)

    # Assert
    expect(master_lecturer_page.table).to_contain_text(employee_id)
