"""Test suite Master Student: add, view, edit, delete (admin office)."""

import allure
from playwright.sync_api import expect

from utils.faker_helper import generate_student


@allure.title("TC-6: 🟡 PENDING — Tambah student baru via Master Student")
def test_add_student(master_student_page):
    # Arrange
    data = generate_student()

    # Act
    master_student_page.add(data)

    # Assert — student baru muncul di tabel
    master_student_page.search_input.fill(data["full_name"])
    expect(master_student_page.page.get_by_text(data["full_name"]).first).to_be_visible()


@allure.title("TC-7: 🟡 PENDING — Lihat detail student via Master Student")
def test_view_student_details(master_student_page):
    # Arrange
    data = generate_student()
    master_student_page.add(data)

    # Act
    master_student_page.details(data["full_name"])

    # Assert — detail field tervalidasi oleh modal
    master_student_page.verify_details(data)


@allure.title("TC-8: 🟡 PENDING — Edit student via Master Student")
def test_edit_student(master_student_page):
    # Arrange
    data = generate_student()
    master_student_page.add(data)
    new_data = {
        "full_name": data["full_name"] + " Edited",
        "email": "edited_" + data["email"],
        "phone": "08123456789",
        "address": "Alamat baru setelah diedit komplit",
    }

    # Act
    master_student_page.edit(data["full_name"], new_data)
    master_student_page.details(new_data["full_name"])

    # Assert — field baru muncul di modal Detail
    page = master_student_page.page
    expect(page.get_by_text(new_data["full_name"]).first).to_be_visible()
    expect(page.get_by_text(new_data["email"]).first).to_be_visible()
    expect(page.get_by_text(new_data["address"]).first).to_be_visible()


@allure.title("TC-9: 🟡 PENDING — Delete student via Master Student")
def test_delete_student(master_student_page):
    # Arrange
    data = generate_student()
    master_student_page.add(data)

    # Act
    master_student_page.delete(data["full_name"])

    # Assert — nama sudah hilang dari halaman
    expect(master_student_page.page.get_by_text(data["full_name"])).not_to_be_visible()
