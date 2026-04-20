"""Test suite Master Course: add course (admin office)."""

import allure
from playwright.sync_api import expect

from utils.faker_helper import generate_course


@allure.title("TC-12: 🟡 PENDING — Tambah course baru via Master Course")
def test_add_course(master_course_page):
    # Arrange
    data = generate_course()

    # Act
    master_course_page.add(data)

    # Assert
    expect(master_course_page.table).to_contain_text(data["course_name"])
